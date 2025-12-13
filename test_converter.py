import unittest
import converter

class TestNumeralConverter(unittest.TestCase):
    # TODO: test different types. decimals, strings, negatives
    def test_basic_conversion(self):
        self.assertEqual(converter.numeral_converter(1), 'I')
        self.assertEqual(converter.numeral_converter(5), 'V')
        self.assertEqual(converter.numeral_converter(10), 'X')
        self.assertEqual(converter.numeral_converter(50), 'L')
        self.assertEqual(converter.numeral_converter(100), 'C')
        self.assertEqual(converter.numeral_converter(500), 'D')
        self.assertEqual(converter.numeral_converter(1000), 'M')

    def test_complex_conversion(self):
        self.assertEqual(converter.numeral_converter(256), 'CCLVI')
        self.assertEqual(converter.numeral_converter(387), 'CCCLXXXVII')
        self.assertEqual(converter.numeral_converter(431), 'CDXXXI')
        self.assertEqual(converter.numeral_converter(789), 'DCCLXXXIX')
        self.assertEqual(converter.numeral_converter(888), 'DCCCLXXXVIII')
        self.assertEqual(converter.numeral_converter(969), 'CMLXIX')
        self.assertEqual(converter.numeral_converter(1987), 'MCMLXXXVII')
        self.assertEqual(converter.numeral_converter(2435), 'MMCDXXXV')
        self.assertEqual(converter.numeral_converter(3707), 'MMMDCCVII')
        self.assertEqual(converter.numeral_converter(3999), 'MMMCMXCIX')

    def test_out_of_range(self):
        self.assertEqual(converter.numeral_converter(0), "Input number 0 is out of range. Please enter a number between 1 and 3999.")
        self.assertEqual(converter.numeral_converter(4000), "Input number 4000 is out of range. Please enter a number between 1 and 3999.")

    def test_wrong_type(self):
        self.assertEqual(converter.numeral_converter(-5), "Input number -5 is out of range. Please enter a number between 1 and 3999.")
        with self.assertRaises(TypeError): converter.numeral_converter(3.5)
        with self.assertRaises(TypeError): converter.numeral_converter("ten")