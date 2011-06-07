from restkit.globals import set_manager, get_manager
try:
    import eventlet
    eventlet.monkey_patch()
    from restkit.manager.meventlet import EventletManager
    set_manager(EventletManager(timeout=60))
except ImportError:
    from restkit import Manager
    set_manager(Manager(max_conn=10))

from fise.client.engines import Engines 
from fise.client.store import Store 

class FISE(object):
    
    def __init__(self, baseuri):
        self.baseuri = baseuri
        
    @property
    def engines(self):
        return Engines(self.baseuri)

    @property
    def store(self):
        return Store(self.baseuri)