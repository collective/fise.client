import os
import restkit

RDFFORMATS = {
    'rdfxml'     : 'application/rdf+xml',
    'rdfjson'    : 'application/rdf+json',
    'rdfntriples': 'text/rdf+nt',
    'turtle'     : 'text/turtle',
}

class FISECommunicator(object):
    
    def __init__(self, baseuri, pool=None):
        self._baseuri = baseuri
        self._instance = None
        self.pool = pool or restkit.SimplePool(keepalive=2)
        
    @property
    def _uri(self):
        return os.path.join(self._baseuri, self._subpath)
        
    @property
    def _resource(self):        
        return restkit.Resource(self._uri, pool_instance=self.pool)