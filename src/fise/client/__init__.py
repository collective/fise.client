from fise.client.engines import Engines 
#from fise.client.store import Store 
#from fise.client.sparql import SPARQL 

class FISE(object):
    
    def __init__(self, baseuri):
        self.baseuri = baseuri
        
    @property
    def engines(self):
        return Engines(self.baseuri)

#    @property
#    def store(self):
#        return Store(self.baseuri)

#    @property
#    def sparql(self):
#        return SPARQL(self.baseuri)
