from fise.client.base import FISECommunicator

class Store(FISECommunicator):
    
    _subpath = 'store'
        
    def __getitem__(self, id):
        pass    
        
    def __setitem__(self, id, payload):
        pass
    
    def metadata(self, id):
        pass
    
    def page(self, id):
        pass        