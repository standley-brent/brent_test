import unittest
import json
from converter import app

class TestNumeralConverter(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_basic_conversion(self):
        basic_cases = [
            (1, 'I'), 
            (5, 'V'), 
            (10, 'X'), 
            (50, 'L'), 
            (100, 'C'), 
            (500, 'D'), 
            (1000, 'M')
        ]
        for num, roman in basic_cases:
            response = self.client.get(f'/romannumeral/?query={num}')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['output'], roman)

    def test_complex_conversion(self):
        test_cases = [
            (256, 'CCLVI'),
            (387, 'CCCLXXXVII'),
            (431, 'CDXXXI'),
            (789, 'DCCLXXXIX'),
            (888, 'DCCCLXXXVIII'),
            (969, 'CMLXIX'),
            (1987, 'MCMLXXXVII'),
            (2435, 'MMCDXXXV'),
            (3707, 'MMMDCCVII'),
            (3999, 'MMMCMXCIX')
        ]
        for num, roman in test_cases:
            response = self.client.get(f'/romannumeral/?query={num}')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['output'], roman)

    def test_out_of_range(self):
        for num in [0, 4000, -5]:
            response = self.client.get(f'/romannumeral/?query={num}')
            self.assertEqual(response.status_code, 400)

    def test_wrong_type(self):
        for val in ['3.5', 'ten']:
            response = self.client.get(f'/romannumeral/?query={val}')
            self.assertEqual(response.status_code, 400)

    def test_range_request(self):
        response = self.client.get('/romannumeral/?min=1&max=3')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['conversions']), 3)
        self.assertEqual(data['conversions'][0]['output'], 'I')
        self.assertEqual(data['conversions'][1]['output'], 'II')
        self.assertEqual(data['conversions'][2]['output'], 'III')

    def test_invalid_range(self):
        for min_val, max_val in [(0, 5), (5, 4000), (10, 5)]:
            response = self.client.get(f'/romannumeral/?min={min_val}&max={max_val}')
            self.assertEqual(response.status_code, 400)

    def test_range_wrong_type(self):
        for min_val, max_val in [('five', 10), (1, 'ten')]:
            response = self.client.get(f'/romannumeral/?min={min_val}&max={max_val}')
            self.assertEqual(response.status_code, 400)

    def test_missing_parameters(self):
        # No parameters
        response = self.client.get('/romannumeral/')
        self.assertEqual(response.status_code, 400)

        # Only min provided
        response = self.client.get('/romannumeral/?min=1')
        self.assertEqual(response.status_code, 400)

        # Only max provided
        response = self.client.get('/romannumeral/?max=10')
        self.assertEqual(response.status_code, 400)

    def test_long_range(self):
        response = self.client.get('/romannumeral/?min=1&max=100')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['conversions']), 100)
        # Check a few values
        self.assertEqual(data['conversions'][0]['output'], 'I')
        self.assertEqual(data['conversions'][49]['output'], 'L')
        self.assertEqual(data['conversions'][99]['output'], 'C')

    def test_wrong_parameter_names(self):
        response = self.client.get('/romannumeral/?minimum=1&maximum=10')
        self.assertEqual(response.status_code, 400)