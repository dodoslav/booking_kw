import requests
import json
from collections import namedtuple

def _json_object_hook(d):
    keys = []
    for k in d.keys():
       if type(k) == type(u'') and k[0] == '_':
            k = 'mod' + k
       try:
            exec ("%s = True" % k) in {}
       except (SyntaxError, NameError, ValueError):
            #print('Invalid field name: %r' % k)
            keys.append('mod_'+k) 
       else:
            keys.append(k) 
    return namedtuple('X', keys)(*d.values())

def json2obj(data): 
    return json.loads(data, object_hook=_json_object_hook)

class FlightBuilder(object):
    """
        Class for converting JSON data about all retrieven flights into python objects. 
    """
    data = None 

    def __init__(self, url):
        self.data = requests.get(url).json()
    
    def build(self):
        return json2obj(json.dumps(self.data))     
        
    
