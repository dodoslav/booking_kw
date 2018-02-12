import unittest
from book_flight import BookFlight,FlightParams
from request_builder import RequestBuilder
import re

class TestBooking(unittest.TestCase):
    def test_return_value(self):
        my_regexp = re.compile("[A-Z0-9]{7}")
        tests = [
            ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--one-way'],
            ['--date', '2018-04-13', '--from', 'LHR', '--to', 'DXB', '--return', '5'],
            ['--date', '2018-04-13', '--from', 'NRT', '--to', 'SYD', '--cheapest', '--bags', '2'],
            ['--date', '2018-04-13', '--from', 'NRT', '--to', 'SYD', '--cheapest'],
            ['--date', '2018-04-13', '--from', 'CPH', '--to', 'MIA', '--fastest', '--bags', '2'],
            ['--date', '2018-04-13', '--from', 'CPH', '--to', 'MIA', '--fastest']
        ]
        for test in tests:
            bf = BookFlight(test)
            bf.getFlights()
            test_token = bf.getReservationCode()
            self.assertTrue(my_regexp.match(test_token) is not None)
    
    def test_request_builder(self):
        url_prefix = "https://api.skypicker.com/flights?v=2&"
        tests = [
            [
                ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--return', '10', '--bags', '2'],
                "asc=1&flyFrom=BCN&to=DUB&dateFrom=13/04/2018&bags=2&dateTo=23/04/2018&limit=200"
            ],
            [
                ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--one-way', '--bags', '2'],
                "asc=1&flyFrom=BCN&to=DUB&dateFrom=13/04/2018&bags=2&limit=200"
            ],
            [
                ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--one-way'],
                "asc=1&flyFrom=BCN&to=DUB&dateFrom=13/04/2018&bags=1&limit=200"
            ],
            [
                ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--fastest'],
                "asc=1&flyFrom=BCN&to=DUB&dateFrom=13/04/2018&bags=1&dateTo=13/04/2018&limit=200"
            ],
            [
                ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--cheapest'],
                "asc=1&flyFrom=BCN&to=DUB&dateFrom=13/04/2018&bags=1&dateTo=13/04/2018&limit=200"
            ]
        ]
            
        for test in tests:    
            params = FlightParams(test[0])
            req = RequestBuilder(params)
            res_url = req.build()
            self.assertEqual(res_url,url_prefix+test[1])

if __name__ == '__main__':
    unittest.main()
