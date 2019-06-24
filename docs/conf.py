# -*- coding: utf-8 -*-
#
# Translate Toolkit documentation build configuration file, created by
# sphinx-quickstart on Mon Mar 26 23:48:04 2012.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.insert(0, os.path.abspath('_ext'))
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions # coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'translate_docs',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Display todo notes. See http://sphinx-doc.org/ext/todo.html#directive-todo
todo_include_todos=True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Translate Toolkit'
copyright = u'2002-2019, Translate'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.3.1'
# The full version, including alpha/beta/rc tags.
release = '2.3.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '_themes/README.rst', 'releases/README.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Missing modules --------------------------------------------------
import sys


class Mock(object):
    VERSION = None

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = type(name, (), {'fixtag': None})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()

MOCK_MODULES = [
    'lucene',
    'PyLucene',
]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

# Needed for _get_pylucene_version() used by translate.search.indexing.__init__
sys.modules['lucene'].VERSION = "2.3.0"
sys.modules['PyLucene'].VERSION = "2.2.0"

autodoc_mock_imports = [
    'aeidon',
    'aeidon.encodings',
    'aeidon.util',
    'aeidon.files',
    'BeautifulSoup',
    'glib',
    'gobject',
    'gtk',
    'iniparse',
    'vobject',
    'xapian',
    'xml',
    'xml.dom',
    'xml.etree',
    'xml.parsers',
]

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx-bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'nosidebar': True,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'TranslateToolkitdoc'


# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
latex_documents = [
  ('index', 'TranslateToolkit.tex', u'Translate Toolkit Documentation',
   u'Translate.org.za', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'translatetoolkit', u'Translate Toolkit Documentation',
     [u'Translate.org.za'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'TranslateToolkit', u'Translate Toolkit Documentation',
   u'Translate.org.za', 'TranslateToolkit', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Coverage checker options -------------------------------------------------

coverage_ignore_modules = []

coverage_ignore_functions = ['main']

coverage_ignore_classes = []

coverage_write_headline = False

# -- Options for Intersphinx -------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/2.7', None),
    'pytest': ('https://docs.pytest.org/en/latest/', None),
    'django': ('http://django.readthedocs.org/en/latest/', None),
    'pootle': ('http://docs.translatehouse.org/projects/pootle/en/latest/', None),
    'guide': ('http://docs.translatehouse.org/projects/localization-guide/en/latest/', None),
}


# -- Options for Exernal links -------------------------------------------------

extlinks = {
    # :role: (URL, prefix)
    'issue': ('https://github.com/translate/translate/issues/%s',
              'issue '),
    'man': ('http://linux.die.net/man/1/%s', ''),
    'wiki': ('http://translate.sourceforge.net/wiki/%s', ''),
    'wp': ('http://en.wikipedia.org/wiki/%s', ''),
}

# -- Options for Linkcheck -------------------------------------------------

# Add regex's here for links that should be ignored.
linkcheck_ignore = [
    'http://your_server.com/filename.html',  # Example URL
    '.*localhost.*',
]
