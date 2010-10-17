try:
    import eventlet
except ImportError:
    HAS_EVENTLET = False
    from restkit import SimplePool 
else:
    HAS_EVENTLET = True
    eventlet.monkey_patch(all=False, socket=True, select=True)
    from restkit.pool.reventlet import EventletPool

from fise.client.engines import Engines 
from fise.client.store import Store 
#from fise.client.sparql import SPARQL 

class FISE(object):
    
    def __init__(self, baseuri):
        self.baseuri = baseuri
        if HAS_EVENTLET:
            pool = EventletPool(keepalive=2, timeout=300)
        else:
            pool = SimplePool(keepalive=2)
        
    @property
    def engines(self):
        return Engines(self.baseuri, pool=self.pool)

    @property
    def store(self):
        return Store(self.baseuri, pool=self.pool)

#    @property
#    def sparql(self):
#        return SPARQL(self.baseuri, pool=self.pool)
