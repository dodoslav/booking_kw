#!/usr/bin/python

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

def main(argv):
    date = ''
    from_place = ''
    to_place = ''
    oneway = False
    cheapest = True
    fastest = False
    bags = 1
    return_days = 0
 
    try:
       #print argv = ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--return', '10', '--bags', '2']
       opts, args = getopt.getopt(argv,"hd:f:t:ocab:",["date=","from=","to=","one-way","cheapest","fastest","bags=","return="])
    except getopt.GetoptError:
       print 'test.py --date <date> --from <from_place> --to <to_place> --one-way --cheapest --fastest --bags <number> --return <days>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
           print 'test.py -i <inputfile> -o <outputfile>'
           sys.exit()
       elif opt in ("--date"):
           date = datetime.strptime(arg, '%Y-%m-%d') 
       elif opt in ("--from"):
           from_place = arg
       elif opt in ("--to"):
           to_place = arg
       elif opt in ("--to"):
           to_place = arg
       elif opt in ("--one-way"):
           oneway = True
       elif opt in ("--fastest"):
           fastest = True
       elif opt in ("--cheapest"):
           cheapest = True
       elif opt in ("--bags"):
           bags = arg
       elif opt in ("--return"):
           return_days = arg
    
    req = RequestBuilder(date,from_place,to_place,return_days,oneway,cheapest,fastest,bags)      
    #req.debug()
    flights = FlightBuilder(req.build()).build()
    min_dur = 100000000
    token = ''
    for i,flight in enumerate(flights.data):
        if flight.duration.total < min_dur:
            min_dur = flight.duration.total
            token = flight.booking_token 
   # import pdb; pdb.set_trace() 
    #print(flight)

    b = Booking(token,bags)
    print(b.do())

if __name__ == "__main__":
    main(sys.argv[1:])
else:
    print("main(['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--return', '10', '--bags', '2'])")
 
