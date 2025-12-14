# Dict of numerals
# Dicts are ordered as of Python 3.7+ and this is Python 3.12

from flask import Flask, jsonify, request
app = Flask(__name__)

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
# Flask route to convert numeral
@app.route('/romannumeral/', methods=['GET'])
def numeral_converter():
    # Parse the input from the query string
    number_input = request.args.get('query')
    original_input = number_input
    try:
        number_input = int(number_input)
    except (TypeError, ValueError):
        # Returns a 400 Bad Request if input is missing or not a number
        return jsonify({'error': 'Expected an integer'}), 400
    roman_result = ''
    lower_bound = 1
    upper_bound = 3999
    if lower_bound <= number_input <= upper_bound:
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
        return jsonify({'input': original_input, 'output': roman_result})
    else:
        raise IndexError(f"Input number {number_input} is out of range. Please enter a number between {lower_bound} and {upper_bound}.")
    
if __name__ == '__main__':
    app.run(debug=True)