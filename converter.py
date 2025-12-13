# Dict of numerals
# Dicts are ordered as of Python 3.7+ and this is Python 3.12

numeral_dict = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def numeral_converter(number_input):
    if not isinstance(number_input, int):
        raise TypeError(f"Expected an integer, but received {type(number_input).__name__}")
    roman_result = ''
    lower_bound = 1
    upper_bound = 3999
    if lower_bound <= number_input <= upper_bound:
        # Looping until number_input is 0
        while number_input > 0:
            # Loop over each numeral in the dict, largest to smallest
            for arabic_num, roman_num in numeral_dict.items():
                # If the input number is larger than the arabic numeral
                if number_input >= arabic_num:
                    # Determine how many times the numeral fits into the input number
                    floor_result = number_input // arabic_num
                    # Subtract that value from the input number
                    number_input = number_input - (floor_result * arabic_num)
                    # Append the corresponding roman numeral to the result
                    roman_result = roman_result + (roman_num * floor_result)
        return roman_result
    else:
        raise IndexError(f"Input number {number_input} is out of range. Please enter a number between {lower_bound} and {upper_bound}.")