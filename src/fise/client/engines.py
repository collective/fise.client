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
        self._check_format(format, parsed)
        headers = {
            'Accept': RDFFORMATS[format],
            'Content-Type': 'text/plain',
        }        
        response = self._resource.post(payload=payload, headers=headers)
        return self._make_result(response, format, parsed)