import sys, getopt
from request_builder import RequestBuilder
from datetime import datetime
from flight import FlightBuilder
from book import Booking
#
# ./book_flight.py --date 2018-04-13 --from BCN --to DUB --one-way
# ./book_flight.py --date 2018-04-13 --from LHR --to DXB --return 5
# ./book_flight.py --date 2018-04-13 --from NRT --to SYD --cheapest --bags 2
# ./book_flight.py --date 2018-04-13 --from CPH --to MIA --fastest

class FlightParams(object):
    """
        Class for processing arguments and keeping them for further processing. 
    """
    _date = ''
    _from_place = ''
    _to_place = ''
    _oneway = True
    _cheapest = True
    _fastest = False
    _bags = 1
    _return_days = 0
    def __init__(self, argv):
     
        try:
           #print argv = ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--return', '10', '--bags', '2']
           opts, args = getopt.getopt(argv,"hd:f:t:ocab:",["date=","from=","to=","one-way","cheapest","fastest","bags=","return="])
        except getopt.GetoptError:
           print 0
           return 
           #print 'test.py --date <date> --from <from_place> --to <to_place> --one-way --cheapest --fastest --bags <number> --return <days>'
           #sys.exit(2)
        for opt, arg in opts:
           if opt == '-h':
               print 'test.py -i <inputfile> -o <outputfile>'
               sys.exit()
           elif opt in ("--date"):
               try:
                   self._date = datetime.strptime(arg, '%Y-%m-%d') 
               except ValueError: 
                   self._values_ok = False        
           elif opt in ("--from"):
               self._from_place = arg
           elif opt in ("--to"):
               self._to_place = arg
           elif opt in ("--one-way"):
               self._oneway = True
           elif opt in ("--fastest"):
               self._fastest = True
               self._cheapest = False
           elif opt in ("--cheapest"):
               self._cheapest = True
           elif opt in ("--bags"):
               self._bags = arg
           elif opt in ("--return"):
               self._return_days = arg
               self._oneway = False
    
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
        return self._return_days
    @date.setter
    def date(self, value):
        self._date = value
    @from_place.setter
    def from_place(self, value):
        self._from_place = value
    @to_place.setter
    def to_place(self, value):
        self._to_place = value
    @oneway.setter
    def oneway(self, value):
        self._oneway = value
    @bags.setter
    def bags(self, value):
        self._bags = value
    @return_days.setter
    def return_days(self, value):
        self._return_days = value


class BookFlight(object):
    """
        Main class for getting flights and getting reservation code based on the chosen booking_token.
    """
    params = None
    req = None
    flights = None
    def __init__(self, args):
        self.params = FlightParams(args)
        self.req = RequestBuilder(self.params)      
    #req.debug()

    def getFlights(self):
        self.flights = FlightBuilder(self.req.build()).build()
    
    def getReservationCode(self):
        if self.flights is None:
            return 0
        min_dur = 100000000
        token = ''
        if self.params.fastest:
            for i,flight in enumerate(self.flights.data):
                if flight.duration.total < min_dur:
                    min_dur = flight.duration.total
                    token = flight.booking_token 
        elif self.params.cheapest:
            flight = self.flights.data[0] # because we are requesting in ascending order
            token = flight.booking_token 
        else:
            print("Neither fastest nor cheapest!")
            token = ""  

        b = Booking(token,self.params.bags)
        self.token = b.do()
        return self.token

            
     
if __name__ == "__main__":
    bf = BookFlight(sys.argv[1:])
    bf.getFlights()
    print(bf.getReservationCode())
