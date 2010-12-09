from restkit import get_default_manager
try:
    import eventlet
except ImportError:
    pass
else:
    from restkit import set_default_manager
    # XXX use EventletConnectionManager

from fise.client.engines import Engines 
from fise.client.store import Store 
#from fise.client.sparql import SPARQL

class FISE(object):
    
    def __init__(self, baseuri):
        self.baseuri = baseuri
        self.pool = get_default_manager()
        
    @property
    def engines(self):
        return Engines(self.baseuri, pool=self.pool)

    @property
    def store(self):
        return Store(self.baseuri, pool=self.pool)

#    @property
#    def sparql(self):
#        return SPARQL(self.baseuri, pool=self.pool)
# use surf.sparql here? 
