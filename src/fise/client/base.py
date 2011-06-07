import os
import restkit
import rdflib

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
        
    @property
    def _uri(self):
        return os.path.join(self._baseuri, self._subpath)
        
    @property
    def _resource(self):        
        return restkit.Resource(self._uri)
    
    def _check_format(self, format, parsed):
        if parsed and format != "rdfxml":
            raise ValueError, "If you want it parsed do not touch the format!"        
        if format not in RDFFORMATS:
            raise ValueError, 'Format "%s" is not possible.' % format
        
    def _check_response(self, response, exception_class, errormsg, code=200):
        if response.status_int != code:
            raise exception_class, '%s Status %i' % (errormsg, 
                                                     response.status_int)
        
    def _make_result(self, response, format, parsed):
        if not parsed:
            return response.body_string()
        graph = rdflib.Graph()
        graph.parse(source=response.body_stream(), format='xml')
        return graph        