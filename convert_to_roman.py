
from numeral_dict import numeral_dict


def convert_to_roman(number_input):
    roman_result = ''
    # Looping until number_input is 0
    while number_input > 0:
        # Loop over each numeral in the dict, largest to smallest
        for arabic_num, roman_num in numeral_dict.items():
            if number_input >= arabic_num:
                # Determine how many times the numeral fits into the input number
                floor_result = number_input // arabic_num
                # Subtract that value from the input number
                number_input = number_input - (floor_result * arabic_num)
                # Append the corresponding roman numeral to the result
                roman_result = roman_result + (roman_num * floor_result)
    return roman_result