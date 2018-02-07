import datetime
class RequestBuilder(object):
    _date = '' # dd/mm/YYYY
    _from_place = ''
    _to_place = ''
    _oneway = False
    _cheapest = False
    _fastest = False
    _bags = 1
    _return = 0
    _version = 3
    
    def __init__(self,date,from_place,to_place,return_days=0,oneway=False,cheapest=False,fastest=False,bags=1):
        self._date = date
        self._from_place = from_place
        self._to_place = to_place
        self._oneway=oneway
        self._cheapest=cheapest
        self._fastest=fastest
        self._bags=bags
        self._return=return_days

    def debug(self):
        print("date: " + self._date.strftime("%d/%m/%y"))
        print("from: " + self._from_place)
        print("to: " + self._to_place)
        print("oneway: " + str(self._oneway))
        print("cheapest: " + str(self._cheapest))
        print("fastest: " + str(self._fastest))
        print("bags: " + str(self._bags))

    def build(self):
        # https://api.skypicker.com/flights?v=3&daysInDestinationFrom=6&daysInDestinationTo=7&flyFrom=49.2-16.61-250km&to=dublin_ie&dateFrom=03/04/2018&dateTo=09/04/2018&typeFlight=return&adults=1&limit=60
        parameters = []
        parameters.append("v=" + str(self._version))
        parameters.append("asc=" + str(int(self._cheapest)))
        parameters.append("flyFrom=" + self._from_place)
        parameters.append("to=" + self._to_place)
        parameters.append("dateFrom="+ self._date.strftime("%d/%m/%Y") )
        parameters.append("bags="+str(self._bags))
        if not self._oneway:
            ret = self._date + datetime.timedelta(days=int(self._return))
            parameters.append("dateTo="+ ret.strftime("%d/%m/%Y"))
        parameters.append("limit=200")
        joined_parameters = '&'.join(parameters)
        return "https://api.skypicker.com/flights?"+joined_parameters 

    @property
    def date(self):
        return self._date
    @property
    def from_place(self):
        return self._from_place
    @property
    def to_place(self):
        return self._to_place
    @property
    def oneway(self):
        return self._oneway
    @property
    def cheapest(self):
        return self._cheapest
    @property
    def fastest(self):
        return self._fastest
    @property
    def bags(self):
        return self._bags
    @property
    def return_days(self):
        return self._return

    # This allows the property to be set
    @date.setter
    def date(self, date):
        self._date = date
    @from_place.setter
    def from_place(self, from_place):
        self._from_place = from_place
    @to_place.setter
    def to_place(self, to_place):
        self._to_place = to_place
    @oneway.setter
    def oneway(self, oneway):
        self._oneway = oneway
    @cheapest.setter
    def cheapest(self, cheapest):
        self._cheapest = cheapest
    @fastest.setter
    def fastest(self, fastest):
        self._fastest = fastest
    @bags.setter
    def bags(self, bags):
        self._bags = bags
    @bags.setter
    def return_days(self, return_days):
        self._return = return_days

    # This allows the property to be deleted
    #@age.deleter
    #def age(self):
    #    del self._age
 
