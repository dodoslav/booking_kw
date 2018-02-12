import datetime
class RequestBuilder(object):
    """
        Class responsible for building url used for retrieving data about flights. 
    """
    params = None   
    url =  "https://api.skypicker.com/flights"
    version = 2
    def __init__(self,params):
        self.params = params

    def debug(self):
        print("date: " + self.params.date.strftime("%d/%m/%y"))
        print("from: " + self.params.from_place)
        print("to: " + self.params.to_place)
        print("oneway: " + str(self.params.oneway))
        print("cheapest: " + str(self.params.cheapest))
        print("fastest: " + str(self.params.fastest))
        print("bags: " + str(self.params.bags))

    def build(self):
        # https://api.skypicker.com/flights?v=3&daysInDestinationFrom=6&daysInDestinationTo=7&flyFrom=49.2-16.61-250km&to=dublin_ie&dateFrom=03/04/2018&dateTo=09/04/2018&typeFlight=return&adults=1&limit=60
        parameters = []
        parameters.append("v=" + str(self.version))
        parameters.append("asc=" + str(int(self.params.cheapest)))
        parameters.append("flyFrom=" + self.params.from_place)
        parameters.append("to=" + self.params.to_place)
        parameters.append("dateFrom="+ self.params.date.strftime("%d/%m/%Y") )
        parameters.append("bags="+str(self.params.bags))
        if not self.params.oneway:
            ret = self.params.date + datetime.timedelta(days=int(self.params.return_days))
            parameters.append("dateTo="+ ret.strftime("%d/%m/%Y"))
        parameters.append("limit=200")
        joined_parameters = '&'.join(parameters)
        return self.url+"?"+joined_parameters 

 
