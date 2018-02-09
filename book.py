import json, requests

from json import loads
from collections import OrderedDict

class Booking(object):
    url = "http://128.199.48.38:8080/booking"
    token = ''
    currency = ''
    #passengers = '{"0":{ "email":["test@test.sk"], "firstName": ["Janko"], "documentID": ["123456"], "lastName": ["Hrasko"], "birthday": ["28/2/1990"], "title": ["Bgr"]}}'
    passengers = '{ "email":"test@test.sk", "firstName": "Janko", "documentID": "123456", "lastName": "Hrasko", "birthday": "1999-2-2", "title": "Mr"}'
    #passengers = '{"0":{ "email":["Missing data for required field."], "firstName": ["Missing data for required field."], "documentID": ["Missing data for required field."],"lastName": ["Missing data for required field."], "birthday": ["Missing data for required field."], "title": ["Missing data for required field."]}}'
    def __init__(self,token,bags,currency="EUR"):
        self.token = token
        self.currency = currency
        self.bags=bags

    def build_params(self):
        return {
            "booking_token":self.token,
            "currency":self.currency,
            "passengers":json.loads(self.passengers, object_pairs_hook=OrderedDict),
            "bags":self.bags
        }

    def do(self):
        #u = self.url+"?booking_token="+self.token
        #print u
        #resp = requests.post(url=u)
        headers = {'content-type': 'application/json'}
        payload = self.build_params()
        resp = requests.post(url=self.url, json=payload, headers=headers)
        data = json.loads(resp.text)
        return data['pnr']

     
