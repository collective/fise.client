import os
import urlparse
from restkit.errors import (
    ResourceNotFound
)
from fise.client.base import (
    FISECommunicator,
    RDFFORMATS,
)

class Store(FISECommunicator):
    
    _subpath = 'store'
        
    def __getitem__(self, cid):
        """Get raw content back from store."""
        headers = {
            'Accept': 'text/plain',
        }        
        path = "raw/%s" % cid
        try:
            response = self._resource.get(path=path, headers=headers)
        except ResourceNotFound, e:
            raise KeyError, cid           
        self._check_response(response, KeyError, 
                             'Cant get content with id %s from fise' % id)
        return response.body_string()
    
    def get(self, cid, default=None):
        try:
            return self[cid]
        except KeyError:
            return default
                
    def __setitem__(self, cid, payload):
        """Adds or updates content to store using given id.
        """ 
        headers = {
            'Content-Type': 'text/plain',
        }        
        path = "content/%s" % cid
        response = self._resource.put(path=path, payload=payload, 
                                      headers=headers)
        self._check_response(response, ValueError, 
                             'Cant put content with id %s to fise' % cid, 
                             code=201)

    def add(self, payload):
        """Adds content to store and let FISE create an ID. Returns new ID.
        """
        headers = {
            'Content-Type': 'text/plain',
        }        
        response = self._resource.post(payload=payload, headers=headers)
        self._check_response(response, ValueError, 
                             'Can not put content to fise', code=201)
        path = urlparse.urlparse(response.headers['Location']).path
        path = path.split('/')
        return path[-1]        
    
    def metadata(self, cid, format='rdfxml', parsed=False):
        """Get extracted rdf+xml metadata of content with given id.
        """
        self._check_format(format, parsed)
        headers = {
            'Accept': RDFFORMATS[format],
        }        
        path = "metadata/%s" % cid
        response = self._resource.get(path=path, headers=headers)
        self._check_response(response, KeyError, 
                             'Cant get metadata with id %s from fise' % cid)
        return self._make_result(response, format, parsed)
    
    def page(self, cid):
        """URL to HTML summary view of the extracted RDF metadata.
        """
        headers = {
            'Accept': 'text/html',
        }        
        path = "page/%s" % cid
        response = self._resource.get(path=path, headers=headers)
        self._check_response(response, KeyError, 
                             'Cant put content with id %s to fise' % cid)
        return response.body_string()