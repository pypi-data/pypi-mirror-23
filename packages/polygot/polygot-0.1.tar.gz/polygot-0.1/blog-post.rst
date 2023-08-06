polygot 
=========================

*Using the readability parser API generate clean HTML and PDF documents of articles found on the web*.

Usage
======

.. code-block:: bash 
   
    
    *CL tool for polygot*
    
    :Author:
        David Young
    
    :Date Created:
        September 28, 2015
    
    Usage:
        polygot url <urlToParse> <destinationFolder> [-s <pathToSettingsFile>]
    
        -h, --help            show this help message
        -v, --version         show version
        -s, --settings        the settings file
        urlToParse            the url of the article to parse and convert to PDF
        destinationFolder     the folder to add the parsed PDF to
    

Installation
============

The easiest way to install polygot us to use ``pip``:

.. code:: bash

    pip install polygot

Or you can clone the `github repo <https://github.com/thespacedoctor/polygot>`__ and install from a local version of the code:

.. code:: bash

    git clone git@github.com:thespacedoctor/polygot.git
    cd polygot
    python setup.py install

To upgrade to the latest version of polygot use the command:

.. code:: bash

    pip install polygot --upgrade


Documentation
=============

Documentation for polygot is hosted by `Read the Docs <http://polygot.readthedocs.org/en/stable/>`__ (last `stable version <http://polygot.readthedocs.org/en/stable/>`__ and `latest version <http://polygot.readthedocs.org/en/latest/>`__).

Tutorial
========

.. todo::

    - add tutorial

