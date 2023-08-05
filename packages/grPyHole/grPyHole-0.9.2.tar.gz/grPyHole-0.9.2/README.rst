PyHole Repository
=================

This is the PyHole general relativity raytracing project repository.

Directory Layout
================

The directory layout is as follows:

- docs:       Sphinx files for the automatically generated API documentation of PyHole. You need to install Sphinx to generate the documentation.
- examples:   Some example files showing how to use PyHole and to start simple projects from.
- gr_pyhole:  The source code of the PyHole python module.
- tests:      Some tests to check correct installation of PyHole for various metric / propagator combinations.
  Contains also reference images of the test results.
- tutorial:   The PyHole tutorial in PDF form along with the code and with some of the solutions for the exercises.
- webgl:      An interactive WebGL based website for black hole visualization using PyHole textures (see Section 7 in the tutorial).


Installation
============

To install PyHole, simply use the pip command. Make sure to use it exactly like this:

    pip install .

from the root directory of this repository.
Alternatively, you can use

    pip install grPyHole

to install the package from PyPI instead of from the source.

Warning: There is another package called PyHole in the python package manager that has nothing to do with black holes. You do not want to install that accidentally by using the name "pyhole" in the pip command!


First steps
===========

For more on first steps and what to do with PyHole, read the tutorial in the tutorial folder.
