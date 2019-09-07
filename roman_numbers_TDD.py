import unittest
import re

class RomanNumber(object):
    numbers = [100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numbers = ['C','XC','L','XL','X','IX','V','IV','I']

    def number_to_roman(self, number):
        if re.match(r'^\d+$', str(number)):
            leftover = number
            roman_number = ''
            for i in range(len(self.numbers)):
                roman_number, leftover = self.add_roman_number(leftover, self.roman_numbers[i], self.numbers[i], roman_number)
        else:
            roman_number = 'Error' 
        return roman_number

    def add_roman_number(self, num, roman, number, roman_number):
        leftover = num

        while leftover >= number:
            roman_number += roman
            leftover -= number
        return roman_number, leftover

class TestRomanNumbers(unittest.TestCase):

    def setUp(self):
        self.roman_number = RomanNumber()
    
    def test_empty_character_to_roman(self):
        roman_number = self.roman_number.number_to_roman('')
        print('Test: \'\'--> '+roman_number)
        self.assertEqual('Error',roman_number)

    def test_str_to_roman(self):
        roman_number = self.roman_number.number_to_roman('&')
        print('Test: & --> '+roman_number)
        self.assertEqual('Error',roman_number)

    def test_one_to_roman(self):
        roman_number = self.roman_number.number_to_roman(1)
        print('Test: 1 --> '+roman_number)
        self.assertEqual('I',roman_number)

    def test_two_to_roman(self):
        roman_number = self.roman_number.number_to_roman(2)
        print('Test: 2 --> '+roman_number)
        self.assertEqual('II',roman_number)

    def test_three_to_roman(self):
        roman_number = self.roman_number.number_to_roman(3)
        print('Test: 3 --> '+roman_number)
        self.assertEqual('III',roman_number)

    def test_four_to_roman(self):
        roman_number = self.roman_number.number_to_roman(4)
        print('Test: 4 --> '+roman_number)
        self.assertEqual('IV',roman_number)

    def test_five_to_roman(self):
        roman_number = self.roman_number.number_to_roman(5)
        print('Test: 5 --> '+roman_number)
        self.assertEqual('V',roman_number)

    def test_seven_to_roman(self):
        roman_number = self.roman_number.number_to_roman(7)
        print('Test: 7 --> '+roman_number)
        self.assertEqual('VII',roman_number)

    def test_nine_to_roman(self):
        roman_number = self.roman_number.number_to_roman(9)
        print('Test: 9 --> '+roman_number)
        self.assertEqual('IX',roman_number)

    def test_ten_to_roman(self):
        roman_number = self.roman_number.number_to_roman(10)
        print('Test: 10 --> '+roman_number)
        self.assertEqual('X',roman_number)

    def test_fourteen_to_roman(self):
        roman_number = self.roman_number.number_to_roman(14)
        print('Test: 14 --> '+roman_number)
        self.assertEqual('XIV',roman_number)

    def test_twenty_three_to_roman(self):
        roman_number = self.roman_number.number_to_roman(23)
        print('Test: 23 --> '+roman_number)
        self.assertEqual('XXIII',roman_number)

    def test_forty_to_roman(self):
        roman_number = self.roman_number.number_to_roman(40)
        print('Test: 40 --> '+roman_number)
        self.assertEqual('XL',roman_number)

    def test_fifty_to_roman(self):
        roman_number = self.roman_number.number_to_roman(50)
        print('Test: 50 --> '+roman_number)
        self.assertEqual('L',roman_number)

    def test_ninety_to_roman(self):
        roman_number = self.roman_number.number_to_roman(90)
        print('Test: 90 --> '+roman_number)
        self.assertEqual('XC',roman_number)

    def test_one_hundred_to_roman(self):
        roman_number = self.roman_number.number_to_roman(100)
        print('Test: 100 --> '+roman_number)
        self.assertEqual('C',roman_number)


if __name__ == "__main__":
    unittest.main()