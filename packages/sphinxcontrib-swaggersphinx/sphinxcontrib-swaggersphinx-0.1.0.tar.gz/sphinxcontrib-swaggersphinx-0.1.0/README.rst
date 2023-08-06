sphinxcontrib-swaggersphinx
############################

A Sphinx extension for documenting Swagger APIs.

.. code:: bash

   pip install sphinxcontrib-swaggersphinx

Requirements
============

* python >= 3.3

Installation
============

This package can be installed using pip:

::

    pip install sphinxcontrib-swaggersphinx


Usage
=====

Include this an extension in your Sphinx ``conf.py``:

.. code:: python

   extensions = ['sphinxcontrib.swaggersphinx']

Then you can use it in your ``.rst`` files to include Swagger documentation:

.. code:: restructuredtext

    .. swaggersphinx:: /path/to/swagger.json

You can include local files (relative to the .rst), local files (full path), or URLs:

.. code:: restructuredtext

    .. swaggersphinx:: /full/path/swagger.json

    .. swaggersphinx:: relative/swagger.json

    .. swaggersphinx:: http://localhost/api/swagger.json
