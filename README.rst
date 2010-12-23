This is the `Python <http://www.python.org/>`_ client for 
`FISE <http://wiki.iks-project.eu/index.php/FISE>`_  (Furtwangen IKS Semantic 
Engine). FISE offers a RESTful API to communicate with.

A good `introduction an overview of FISE features <http://blogs.nuxeo.com/dev/2010/08/introducing-fise-the-restful-semantic-engine.html>`_ 
has been written by Olivier Grisel. 

FISE offers are basically three methods of interaction:

engines
    stateless interface, submit content to the fise engines and get the 
    resulting enhancements formatted as RDF at once without storing anything on 
    the server-side.

store
    Upload content to the store and in a second step get the enhancements back.
    
sparql
    access FISE as a SPARQL endpoint (W3C conform).
    
This API covers ``engines`` and ``store``. Sparql queries are best done by using 
existing library ``SuRF <http://packages.python.org/SuRF/>``_ which is installed 
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



    
