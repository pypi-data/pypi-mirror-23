grymp
=====

.. image:: https://img.shields.io/pypi/status/grymp.svg
   :target: https://pypi.python.org/pypi/grymp
.. image:: https://img.shields.io/pypi/v/grymp.svg
   :target: https://pypi.python.org/pypi/grymp
.. image:: https://img.shields.io/pypi/pyversions/grymp.svg
   :target: https://pypi.python.org/pypi/grymp
.. image:: https://travis-ci.org/gebn/grymp.svg?branch=master
   :target: https://travis-ci.org/gebn/grymp
.. image:: https://coveralls.io/repos/github/gebn/grymp/badge.svg?branch=master
   :target: https://coveralls.io/github/gebn/grymp?branch=master
.. image:: https://landscape.io/github/gebn/grymp/master/landscape.svg?style=flat
   :target: https://landscape.io/github/gebn/grymp/master

Automate the processing of Grym/vonRicht releases. Please note: this module does *not* download anything; it only speeds up moving around and renaming existing files.

Installation
------------

::

    $ pip install grymp

Examples
--------

Process a release located at ``~/Release.Name-Grym``. The feature will be placed in ``/tmp/features``, and the extras in ``/tmp/extras``:

::

    $ grymp -f /tmp/features -e /tmp/extras ~/Release.Name-Grym

To only process the feature *or* extras, only pass the ``-f`` or ``-e`` option (with a path) respectively.

Usage
-----

::

    $ grymp -h
    usage: grymp [-h] [-V] [-v] [-i] [-o] [-k] [-f FEATURE] [-e EXTRAS]
                 base [base ...]

    Automate the processing of Grym/vonRicht releases

    positional arguments:
      base                  one or more root directories of releases, each
                            containing a feature

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -v, --verbosity       increase output verbosity
      -i, --interactive     prompt before each operation affecting the filesystem
      -o, --overwrite       overwrite files without asking
      -k, --keep            keep original files; only has an effect if they were
                            copied because the destination was on a different
                            filesystem
      -f FEATURE, --feature FEATURE
                            marshal the feature into this directory (it must
                            exist)
      -e EXTRAS, --extras EXTRAS
                            marshal the extras into a new subdirectory within this
                            directory, named after the feature


