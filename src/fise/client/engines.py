import rdflib
from fise.client.base import (
    FISECommunicator,
    RDFFORMATS,
)

class Engines(FISECommunicator):
    
    _subpath = 'engines'
    
    def __call__(self, payload, format='rdfxml', parsed=False):
        """Submit payload to FISE engines and get enhancements back.
        
        :param payload: content for submission to fise. 
        :type payload:  String, Unicode or UTF8, Content-Type 'text/plain'
        :param format: format to be requested. Does not work toegther with 
                       'parsed'. 
        :type format: String, one out of 'rdfxml', 'rdfjson', 'rdfntriples', 
                      'turtle'.
        :param parsed: get the result as python 'rdflib.Graph' instance. 
        :rtype: String or rdflib.Graph instance   
        """ 
        if parsed and format != "rdfxml":
            raise ValueError, "If you want it parsed do not touch the format!"
        self._check_format(format)
        headers = {
            'Accept': RDFFORMATS[format],
            'Content-Type': 'text/plain',
        }        
        result = self._resource.post(payload=payload, headers=headers)
        if not parsed:
            return result.body_string()
        graph = rdflib.Graph()
        graph.parse(source=result.body_stream(), format=RDFFORMATS[format])
        return graph