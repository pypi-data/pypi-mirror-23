|mistletoe|
===========

|Build Status| |Coverage Status|

mistletoe is a Markdown parser in pure Python, designed to be fast, modular and fully customizable.

mistletoe is not simply a Markdown-to-HTML transpiler. It is designed, from the start, to parse
Markdown into an abstract syntax tree. You can swap out renderers for different output formats,
without touching any of the core components.

Remember to spell mistletoe in lowercase!

Features
--------

-  **Fast**: mistletoe strives to be as fast as the `fastest
   implementation <https://github.com/lepture/mistune>`__ currently available: that is, over 3 times
   faster than `Python-Markdown <https://github.com/waylan/Python-Markdown>`__, and over 4 times
   faster than `Python-Markdown2 <https://github.com/trentm/python-markdown2>`__.

   -  mistletoe uses Python generators under the hood. If you choose not to render some lower-level
      tokens, they will not get parsed: a huge performance improvement.

   -  mistletoe uses a streaming algorithm to parse input files. Together with generators, this
      means that mistletoe is light on memory, and by nature can deal with very large input files.

-  **Modular**: mistletoe is designed with modularity in mind. Its initial goal is to provide a
   clear and easy API to extend upon.

-  **Customizable**: mistletoe wants to solve the problem: "my Markdown is better than yours."
   Markdown's syntax is, and should be, a matter of personal preference. As such, mistletoe does not
   make sweeping decisions, but leaves much in the hands of the user.

Installation
------------

mistletoe is tested on Python 3.5, Python 3.6, and PyPy 5.8.0. Install mistletoe with pip:

.. code:: sh

    pip3 install mistletoe

Alternatively, clone the repo:

.. code:: sh

    git clone https://github.com/miyuchina/mistletoe.git
    cd mistletoe
    pip3 install -e .

Usage
-----

>From the command-line
~~~~~~~~~~~~~~~~~~~~~

pip installation enables mistletoe's commandline utility. Type the following directly into your
shell:

.. code:: sh

    mistletoe foo.md

This will transpile ``foo.md`` into HTML, and dump the output to stdout. To save the HTML, direct
the output into a file:

.. code:: sh

    mistletoe foo.md > out.html

Running ``mistletoe`` without specifying a file will land you in interactive mode. Like Python's
REPL, interactive mode allows you to test how your Markdown will be interpreted by mistletoe:

::

    mistletoe [version 0.1 alpha] (interactive)
    Type Ctrl-D to complete input, or Ctrl-C to exit.
    >>> some **bold text**
    ... and some *italics*
    ... ^D
    <html>
    <body>
    <p>some <strong>bold text</strong> and some <em>italics</em></p>
    </body>
    </html>
    >>>

Typing ``Ctrl-D`` tells mistletoe to interpret your input. ``Ctrl-C`` exits the program.

Basic usage
~~~~~~~~~~~

Here's how you can use mistletoe in a Python script:

.. code:: python

    import mistletoe

    with open('foo.md', 'r') as fin:
        rendered = mistletoe.markdown(fin)

``mistletoe.markdown()`` uses mistletoe's default settings: allowing HTML mixins and rendering to
HTML.

Okay, give it to me straight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's how you would manually specify extra tokens and a renderer for mistletoe. In the following
example, we add ``HTMLBlock`` and ``HTMLSpan`` to the normal parsing process, and use
``HTMLRenderer`` to render the AST:

.. code:: python

    from mistletoe import Document
    from mistletoe.html_token import Context
    from mistletoe.html_renderer import render

    with open('foo.md', 'r') as fin:
        with Context():
            rendered = render(Document(fin))

... or an even more verbose version:

.. code:: python

    from mistletoe import Document
    from mistletoe.html_token import Context
    from mistletoe.html_renderer import HTMLRenderer

    with open('foo.md', 'r') as fin:
        with Context():
            token = Document(fin)
            renderer = HTMLRenderer()
            rendered = renderer.render(token)

Developer's Guide
-----------------

Although chances of mistletoe undergoing another crazy overhaul is very limited, its API is not
stabilized yet. That said, however, here's an example to add GitHub-style wiki links to the parsing
process, and provide a renderer for this new token.

A new token
~~~~~~~~~~~

GitHub wiki links are span-level tokens, meaning that they reside inline, and don't really look like
chunky paragraphs. To write a new span-level token, all we need to do is make a subclass of
``SpanToken``:

.. code:: python

    from mistletoe.span_token import SpanToken

    class GitHubWiki(SpanToken):
        pass

mistletoe uses regular expressions to search for span-level tokens in the parsing process. As a
refresher, GitHub wiki looks something like this: ``[[alternative text | target]]``. We define a
class variable, ``pattern``, that stores the compiled regex:

.. code:: python

    class GitHubWiki(SpanToken):
        pattern = re.compile(r"(\[\[(.+?)\|(.+?)\]\])")
        def __init__(self, raw):
            pass

For spiritual guidance on regexes, refer to `xkcd <https://xkcd.com/208/>`__ classics. For an actual
representation of this author parsing Markdown with regexes, refer to this brilliant
`meme <http://www.greghendershott.com/img/grumpy-regexp-parser.png>`__ by `Greg
Hendershott <http://www.greghendershott.com/2013/11/markdown-parser-redesign.html>`__.

mistletoe's span-level tokenizer will search for our pattern. When it finds a match, it will pass in
the first matching group as argument (``raw``). In our case, this happens to be the entire link with
enclosing brackets, so we still need to do some dirty string manipulation:

.. code:: python

    alt, target = raw[2:-2].split('|', 1)

``alt`` can also contain other span-level tokens. For example, ``[[*alt*|link]]`` is a GitHub link
with an ``Emphasis`` token as its child. To parse child tokens, simply pass it to the ``super``
constructor, and save off all the additional attributes we need:

.. code:: python

    super().__init__(alt)
    self.target = target

After some cleaning-up, this is what our new token class looks like:

.. code:: python

    from mistletoe.span_token import SpanToken

    class GitHubWiki(SpanToken):
        pattern = re.compile(r"(\[\[(.+?)\|(.+?)\]\])")
        def __init__(self, raw):
            alt, target = raw[2:-2].split('|', 1)
            super().__init__(alt.strip())
            self.target = target.strip()

A new renderer
~~~~~~~~~~~~~~

If we only need to use GitHubWiki only once, we can simply create an ``HTMLRenderer`` instance, and
append a ``render()`` function to its ``render_map``. However, let's suppose we are writing a plugin
for others to use. We only need to subclass ``HTMLRenderer`` to provide reusability:

.. code:: python

    from mistletoe.html_renderer import HTMLRenderer

    class GitHubWikiRenderer(HTMLRenderer):
        def __init__(self, preamble=''):
            super().__init__(preamble)
            self.render_map['GitHubWiki'] = self.render_github_wiki

The ``super`` constructor call inherits the original ``render_map`` from ``HTMLRenderer``. We then
add an additional entry to the ``render_map``, pointing to our new render method:

.. code:: python

    def render_github_wiki(self, token):
        template = '<a href="{target}">{inner}</a>'
        target = token.target
        inner = self.render_inner(token)
        return template.format(target=target, inner=inner)

``self.render_inner(token)`` recursively calls ``render()`` on the child tokens of ``token``, then
joins them together as a single string. Cleaning up, we have our new renderer class:

.. code:: python

    import urllib.parse
    from mistletoe.html_renderer import HTMLRenderer

    class GitHubWikiRenderer(HTMLRenderer):
        def __init__(self, preamble=''):
            super().__init__(preamble)
            self.render_map['GitHubWiki'] = self.render_github_wiki

        def render_github_wiki(self, token):
            template = '<a href="{target}">{inner}</a>'
            target = urllib.parse.quote_plus(token.target)
            inner = self.render_inner(token)
            return template.format(target=target, inner=inner)

Putting everything together
~~~~~~~~~~~~~~~~~~~~~~~~~~~

mistletoe's span-level tokenizer looks for tokens in the ``__all__`` variable of ``span_token``
module. The magic of injecting our ``GitHubWiki`` token into the parsing process, then, is pretty
straight-forward:

.. code:: python

    import mistletoe

    mistletoe.span_token.GitHubWiki = GitHubWiki
    mistletoe.span_token.__all__.append('GitHubWiki')

When we render, we create a new instance of ``GitHubWikiRenderer``, and call ``render()`` on the
input token:

.. code:: python

    rendered = GitHubWikiRenderer().render(token)

We are technically good to go at this point. However, the code above messes up ``span_token``'s
global namespace quite a bit. The actual ``github_wiki`` module in the ``plugins/`` directory uses
Python's context manager:

.. code:: python

    class Context(object):
        def __init__(self):
            self.renderer = GitHubWikiRenderer

        def __enter__(self):
            mistletoe.span_token.GitHubWiki = GitHubWiki
            mistletoe.span_token.__all__.append('GitHubWiki')
            return self

        def __exit__(self, exception_type, exception_val, traceback):
            del mistletoe.span_token.GitHubWiki
            mistletoe.span_token.__all__.remove('GitHubWiki')

        def render(self, token):
            return self.renderer().render(token)

This allows us to use our new token like this:

.. code:: python

    from mistletoe import Document
    from plugins.github_wiki import Context

    with open('foo.md', 'r') as fin:
        with Context() as c:
            rendered = c.render(Document(fin))

For more info, take a look at the ``html_renderer`` module in mistletoe. The docstrings might give
you a more granular idea of customizing mistletoe to your needs.

Why mistletoe?
--------------

For me, the question becomes: why not `mistune <https://github.com/lepture/mistune>`__? My original
motivation really has nothing to do with starting a competition. Here's a list of reasons I created
mistletoe in the first place:

-  I am interested in a Markdown-to-LaTeX transpiler in Python.
-  I want to write more Python. Specifically, I want to try out some bleeding edge features in
   Python 3.6, which, in turn, makes me love the language even more.
-  I am stuck at home during summer vacation without an internship, which, in turn, makes me realize
   how much I love banging out software from scratch, all by myself. Also, global warming keeps me
   indoors.
-  I have long wanted to write a static site generator, *from scratch, by myself.* One key piece of
   the puzzle is my own Markdown parser. "How hard could it be?" (well, quite a lot harder than I
   expected.)
-  "For fun," says David Beasley.

mistletoe shares with mistune the goal that Markdown parsers should be fast, and other parser
implementations in Python leaves much to be desired.

Here's two things mistletoe does differently from mistune:

-  Per its `readme <https://github.com/lepture/mistune>`__, mistune will always be a single-file
   script. mistletoe breaks its functionality into modules.
-  mistune, as of now, can only render Markdown into HTML. It is relatively trivial to write a new
   renderer for mistletoe.

The implications of these are quite profound, and there's no definite I'm- better-than-you answer.
Mistune is near perfect if one wants what it provides: I have used mistune extensively in the past,
and had a great experience. If you want more control, however, give mistletoe a try.

My hunch is that mistletoe *will be slower* than a fully optimized mistune *when feature complete.*
This is because separating components into modules creates quite a bit of lookup overhead, that is
inevitable with mistletoe but not a concern with mistune.

As of now mistletoe performs marginally better on CPython 3.6 than mistune. Parsing
`README.md <https://github.com/jquery/jquery/blob/master/README.md>`__ of the jQuery project (whose
syntax mistletoe fully supports) 1000 times shows that mistletoe is as fast as mistune. Using PyPy
(whose function overheads are better optimized than CPython), mistune takes about 7 seconds to
complete the said task, whereas mistletoe takes less than 5 seconds.

This, however, is not indicative of final performance difference, as mistletoe is not yet feature
complete.

Finally, to quote `Raymond Hettinger <https://www.youtube.com/watch?v=voXVTjwnn-U>`__:

    If you make something successful, you don't have to make something else unsuccessful.

There is infinite fun and inspiration to be found in reinventing the wheels, and proclaiming one's
supremacy to satisfy his or her ego, while holding those who came before in disrespect, is
prioritizing the trivial.

Copyright & License
-------------------

-  mistletoe's logo uses artwork by Daniele De Santis, under `CC BY
   3.0 <https://creativecommons.org/licenses/by/3.0/us/>`__.
-  The font used in the logo is `Cedarville
   Cursive <https://fonts.google.com/specimen/Cedarville+Cursive>`__, released under `Open Font
   License <http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web>`__.
-  mistletoe is released under `GNU GPLv3 <LICENSE>`__, a copyleft license.

.. |mistletoe| image:: https://cdn.rawgit.com/miyuchina/mistletoe/3f0125f1/logo.svg
.. |Build Status| image:: https://travis-ci.org/miyuchina/mistletoe.svg?branch=master
   :target: https://travis-ci.org/miyuchina/mistletoe
.. |Coverage Status| image:: https://coveralls.io/repos/github/miyuchina/mistletoe/badge.svg
   :target: https://coveralls.io/github/miyuchina/mistletoe?branch=master


