from fise.client.base import (
    FISECommunicator,
    RDFFORMATS,
)

class Engines(FISECommunicator):
    
    _subpath = 'engines'
    
    def __call__(self, payload, format='rdfxml'):
        if format not in RDFFORMATS:
            raise ValueError, 'Format "%s" is not possible.' % format
        headers = {
            'Accept': RDFFORMATS[format],
            'Content-Type': 'text/plain',
        }        
        result = self._resource.post(payload=payload, headers=headers)
        return result.body_string()