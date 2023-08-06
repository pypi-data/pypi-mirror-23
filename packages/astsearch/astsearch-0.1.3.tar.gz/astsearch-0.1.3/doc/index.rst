ASTsearch |version|
===================

ASTsearch is an intelligent search tool for Python code.

To get it::

    pip install astsearch

To use it::

    # astsearch pattern [path]
    astsearch "?/?"  # Division operations in all files in the current directory

.. program:: astsearch

.. option:: pattern

   A search pattern, using ``?`` as a wildcard to match anything. The pattern
   must be a valid Python statement once all ``?`` wilcards have been replaced
   with a name.

.. option:: path

   A Python file or a directory in which to search. Directories will be searched
   recursively for ``.py`` and ``.pyw`` files.

Contents:

.. toctree::
   :maxdepth: 2

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

