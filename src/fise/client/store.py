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
        """Adds content to store using given id.
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
        response = self._resource.post(path=path, payload=payload, 
                                       headers=headers)
        path = urlparse.urlparse(response.headers['Location']).path
        path = path.split('/')
        if len(path) < 3:
            raise ValueError, 'Location path to short.'
        return path[-1]        
    
    def metadata(self, id):
        """Get extracted rdf+xml metadata of content with given id.
        """
        headers = {
            'Accept': RDFFORMATS['rdfxml'],
        }        
        path = "rmetadata/%s" % id
        return self._resource.get(path=path, headers=headers)
    
    def page(self, id):
        """HTML summary view of the extracted RDF metadata.
        """
        pass        