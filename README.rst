This is the `Python <http://www.python.org/>`_ client for Semantic 
Engine `Apache Stanbol FISE <http://incubator.apache.org/stanbol/>`_ (see also
the old `IKS-WIKI <http://wiki.iks-project.eu/index.php/FISE>`_). 
Edutainment:  Watch the `Video by Olivier Grisel <http://blogs.nuxeo.com/dev/2010/08/introducing-fise-the-restful-semantic-engine.html>`_
 
FISE offers a RESTful API with basically three methods of interaction:

engines
    stateless interface, submit content to the fise engines and get the 
    resulting enhancements formatted as RDF at once without storing anything on 
    the server-side.

store
    Upload content to the store and in a second step get the enhancements back.
    
sparql
    access FISE as a SPARQL endpoint (W3C conform).
    
This API covers ``engines`` and ``store``. Sparql queries are best done by using 
existing library `SuRF <http://packages.python.org/SuRF/>`_ which is installed 
as a dependecy with this package.      
    
Python API
==========

Initialize::

    >>> from fise.client import FISE
    >>> fise = FISE('http://localhost:8080/')

Use the engines::    
    
    >>> somedoc = u"This is an example text."
    >>> fise.engines(somedoc)
    <xml...>
    
    >>> fise.engines(somedoc, format='rdfjson')
    jsonresponse

Use the store, first store content (only plain text is accepted for now)::
    
    >>> id = 'test123'
    >>> fise.store.content[id] = payload

Next get the text back::    
    
    >>> fise.store.content[id]
    u"This is an example text."

Then get the metadata::
    
    >>> fise.store.metadata(id)
    <RDF>
    
And FISE special feature: Get an HTML page about the content::    

    >>> fise.store.page(id)
    <HTML>

Install
=======

Demo Installation
-----------------

If you want to try this package as is this is probably a good starting point.

Fetch the package sources and unpack them in a directory of your choice::

    $ wget http://pypi.python.org/packages/source/f/fise.client/bda.cache-[VERSION].tar.gz
    $ tar xzf bda.cache-[VERSION].tar.gz
    $ cd bda.cache-[VERSION]

Python 2.6 or 2.7 needs to be available. 

To avoid collisions with packages already installed in your pre-installed python
virtualenv is used (instead of easy_install on Debian/Ubuntu 
``sudo apt-get install python-virtual`` works fine)::

    $ easy_install virtualenv
    $ python2.6 virtualenv  --no-site-packages py
    
Bootstrap and run the contained buildout. This fetches FISE early adopter 
release and provides a start script for FISE. It installs all Python 
dependencies of fise.client and provides a script to run all tests and a Python 
shell with all packaged installed::  

    $ ./py/bin/python bootstrap.py
    $ ./bin/buildout

Start the FISE semantic engine.

    $ ./bin/fise-instance
    
Now connect with a webbrower to 
`http://localhost:8080/ <http://localhost:8080/>`_, the FISE web-frontend.

Running the tests shows if everything working as expected (needs a running 
``fise-instance``)::

    $ ./bin/tests
    
Start a Python shell with fise.client included::

    $ ./bin/py
        
    >>> from fise.client import FISE
    >>>
    
Installation within existing environment
----------------------------------------     

To add this package to an existing environment do::

    $ easy_install fise.client

Or if your using ``zc.buildout`` add a line to the eggs in your 
``buildout.cfg`` and re-run buildout:: 

    [buildout]    
    ...
    eggs = 
    ...
        fise.client
    ...
    
Or if your'e writing an own python-package add it to the ``install_requires`` 
section.

Changelog
=========

1.0
---
- initial code, tests and documentation

Copyright, License, Contributors
================================

copyright BlueDynamics Alliance, 2010

This package is provided under the OSI-approved OpenSource License 
`Python Software Foundation License 
<http://opensource.org/licenses/PythonSoftFoundation.php>`_ (as Python itself 
is).

Contributors:

- funded by `IKS-Project early adopters program 
  <http://wiki.iks-project.eu/index.php/About>`_
  
- Jens Klein <jens@bluedynamics.com>, Klein & Partner KG: initial code, tests, 
  documentation and first release.