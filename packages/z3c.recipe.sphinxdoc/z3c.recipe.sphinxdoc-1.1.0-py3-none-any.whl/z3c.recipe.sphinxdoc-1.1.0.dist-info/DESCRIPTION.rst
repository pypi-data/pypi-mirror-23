======================
 z3c.recipe.sphinxdoc
======================

Introduction
============

This buildout recipe aids in the generation of documentation for the
zope.org website from restructured text files located in a package.
It uses Sphinx to build static html files which can stand alone as a
very nice looking website.

Usage Instructions
==================

Suppose you have a package called ``z3c.form``.  In the ``setup.py``
for ``z3c.form`` it is recommended that you add a ``docs`` section
to the extras_require argument.  It should look something like this::

    extras_require = dict(
        docs = ['Sphinx',
                'z3c.recipe.sphinxdoc']
        )

Then in the buildout.cfg file for your package, add a ``docs`` section
that looks like this::

  [docs]
  recipe = z3c.recipe.sphinxdoc
  eggs = z3c.form [docs]

Be sure to include it in the parts, as in::

  [buildout]
  develop = .
  parts = docs

Now you can rerun buildout.  The recipe will have created an
executable script in the bin directory called ``docs``.

This script will run the Sphinx documentation generation tool on your
source code.  By default, it expects there to be an ``index.rst`` file
in the source code.  In this case, ``index.rst`` would have to be in
``src/z3c/form/index.rst``.  This file can be a standard restructured
text file, and can use all the sphinx goodies.  For example, your
``index.txt`` might look like this::

  Welcome to z3c.form's documentation!
  ====================================

  Contents:

  .. toctree::
     :maxdepth: 2

     README

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

You should read the documentation for Sphinx to learn more about it.
It is available here: http://sphinx.pocoo.org/

Now you should be able to run the ``docs`` script::

  $ ./bin/docs

This generates all the documentation for you and placed it in the
parts directory.  You can then open it up in firefox and take a look::

  $ firefox parts/docs/z3c.form/build/index.html

Additional Options
==================

By default, this recipe generates documentation that looks like the
new zope website ( http://new.zope.org ) by overriding the default
layout template and css file used by sphinx.  You can modify this
behavior with options in your buildout configuration.

Give me back Sphinx's default look!
-----------------------------------

To get back the default look of sphinx, you could use a configuration
like this::

  [docs]
  recipe = z3c.recipe.sphinxdoc
  eggs = z3c.form [docs]
  default.css =
  layout.html =

I want my own custom look
-------------------------

You can also specify your own layout template and css like so::

  [docs]
  recipe = z3c.recipe.sphinxdoc
  eggs = z3c.form [docs]
  default.css = http://my.own.website.com/mystyles/some-theme.css
  layout.html = /path/to/layout.html

Note that you can either specify a path on the local file system or a
url to an external css file.

Use sphinx extension modules
----------------------------

Sphinx provides a set of extensions, for example ``sphinx.ext.autodoc``
or ``sphinx.ext.doctest``. To use such an extension change your
configuration like::

  [docs]
  recipe = z3c.recipe.sphinxdoc
  eggs = z3c.form [docs]
  extensions = sphinx.ext.autodoc sphinx.ext.doctest

Arbitrary Configuration
-----------------------

Sphinx and its extensions offer many configuration options. You can
specify any of those by using the ``extra-conf`` option. This option
takes a sequence of lines that are simply inserted into the generated
``conf.py``. Anything you specify here will override other settings
this recipe established (just watch your leading line indentation)::

  [docs]
  recipe = z3c.recipe.sphinxdoc
  eggs = z3c.form [docs]
  extensions = sphinx.ext.autodoc
               sphinx.ext.todo
               sphinx.ext.viewcode
               sphinx.ext.intersphinx
               repoze.sphinx.autointerface
               sphinxcontrib.programoutput
  default.css =
  layout.html =
  extra-conf =
           autodoc_default_flags = ['members', 'show-inheritance',]
           autoclass_content = 'both'
           intersphinx_mapping = {
           'python':  ('http://docs.python.org/2.7/', None),
           'boto': ('http://boto.readthedocs.org/en/latest/', None),
           'gunicorn': ('http://docs.gunicorn.org/en/latest/', None),
           'pyquery': ('http://packages.python.org/pyquery/', None) }
           intersphinx_cache_limit = -1
           todo_include_todos = True

           # The suffix of source filenames. Override back to txt.
           source_suffix = '.txt'

           # Choose an entire theme. Note that we disabled layout.html
           # and default.css.
           html_theme = 'classic'


=========
 CHANGES
=========

1.1.0 (2017-07-05)
==================

- Add support for Python 3.4, 3.5 and 3.6 and PyPy.

- Remove support for Python 2.6 and 3.3.

- Change the default source suffix from ``.txt`` to ``.rst``. You can
  override this using the new ``extra-conf`` setting.

- Add the ability to specify arbitrary configuration in the
  ``extra-conf`` setting. This is useful for things like configuring
  extensions, overriding the defaults set by this recipe, and
  configuring a sphinx theme.

- Stop forcing a value of ``default.css`` for ``html_style`` even when
  the ``default.css`` setting is configured to an empty value. This
  makes it possible to use ``html_theme`` to set a sphinx theme, and
  it properly lets the default Sphinx theme be used (by setting both
  ``default.css`` and ``layout.html`` to empty values).

- Ignore bad eggs in the documentation working set. Previously they
  would raise internal errors without any explanation. Now, they log a
  warning pinpointing the bad egg. Fixes `issue 6
  <https://github.com/zopefoundation/z3c.recipe.sphinxdoc/issues/6>`_.


1.0.0 (2013-02-23)
==================

- Added Python 3.3 support.

- Bug: fix layout directory if layout is overriden by user

0.0.8 (2009-05-01)
==================

- Feature: Added new option `doc-eggs` which specifies the list of eggs for
  which to create documentation explicitely.

- Feature: Changed building behavior so that the documentation for each
  package is built in its own sub-directory.

- Feature: Added new option `extensions` which takes a whitespace
  separated list of sphinx extension modules. This extensions can be
  used to build the documentation.

0.0.7 (2009-02-15)
==================

- Bug: fix python 2.4 support

- Bug: fix broken srcDir path generation for windows

0.0.6 (2009-01-19)
==================

- Feature: Allow you to specify a url or local file path to your own
  default.css and layout.html files.

0.0.5 (2008-05-11)
==================

- Initial release.


