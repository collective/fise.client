import os
import urlparse
from restkit.errors import ResourceError
from fise.client.base import (
    FISECommunicator,
    RDFFORMATS,
)

class Store(FISECommunicator):
    
    _subpath = 'store'
        
    def __getitem__(self, id):
        """Get raw content back from store."""
        headers = {
            'Accept': 'text/plain',
        }        
        path = "raw/%s" % id
        response = self._resource.get(path=path, headers=headers)
        return response.body_string()
        
    def __setitem__(self, id, payload):
        """Adds or updates content to store using given id.
        """ 
        headers = {
            'Content-Type': 'text/plain',
        }        
        path = "content/%s" % id
        self._resource.put(path=path, payload=payload, headers=headers)

    def add(self, payload):
        """Adds content to store and let FISE create an ID. Returns new ID.
        """
        headers = {
            'Content-Type': 'text/plain',
        }        
        response = self._resource.post(payload=payload, headers=headers)
        path = urlparse.urlparse(response.headers['location']).path
        path = path.split('/')
        return path[-1]        
    
    def metadata(self, id, format='rdfxml', parsed=False):
        """Get extracted rdf+xml metadata of content with given id.
        """
        self._check_format(format, parsed)
        headers = {
            'Accept': RDFFORMATS[format],
        }        
        path = "metadata/%s" % id
        response = self._resource.get(path=path, headers=headers)
        return self._make_result(response, format, parsed)
    
    def page(self, id):
        """URL to HTML summary view of the extracted RDF metadata.
        """
        headers = {
            'Accept': 'text/html',
        }        
        path = "page/%s" % id
        response = self._resource.get(path=path, headers=headers)
        return response.body_string()
