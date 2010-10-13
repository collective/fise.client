import os
import restclient

class FISECommunicator(object):
    
    def __init__(self, baseuri, transport=None):
        self._baseuri = baseuri
        self._instance = None
        self.transport = transport
        
    @property
    def _uri(self):
        return os.path.join(self._baseuri, self._subpath)
        
    @property
    def _resource(self):        
        if self._instance is None:  
            self._instance = restclient.Resource(self._uri, 
                                                 transport=self.transport)
        return self._instance