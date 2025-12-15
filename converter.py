from concurrent.futures import ProcessPoolExecutor
from flask import Flask, jsonify, request
from utils.convert_to_roman import convert_to_roman
app = Flask(__name__)

# Flask route to convert numeral
@app.route('/romannumeral/', methods=['GET'])
    
def numeral_converter():
    lower_bound = 1
    upper_bound = 3999

    # 1. 'query' paramater given, single conversion wanted
    query = request.args.get('query')
    if query is not None:
        try:
            number_input = int(query)
        except ValueError:
            return jsonify({'error': 'Expected an integer'}), 400

        if  lower_bound <= number_input <= upper_bound:
            return jsonify({'input': query, 'output': convert_to_roman(number_input)})
        else:
            return jsonify({'error': f"Input number {number_input} is out of range. Please enter a number between {lower_bound} and {upper_bound}."}), 400
        
    # 2. 'min' & 'max' parameters given: range wanted
    min_val = request.args.get('min')
    max_val = request.args.get('max')

    if min_val is not None and max_val is not None:
        try:
            min_val = int(min_val)
            max_val = int(max_val)
        except ValueError:
            return jsonify({'error': 'Min and max must be integers'}), 400

        if min_val < lower_bound or max_val > upper_bound or min_val > max_val:
            return jsonify({'error': f'Invalid range. Ensure {lower_bound} <= min <= max <= {upper_bound}'}), 400

        # Create list of numbers to convert
        numbers = list(range(min_val, max_val + 1))

        # Use ProcessPoolExecutor for parallel conversion
        with ProcessPoolExecutor(max_workers=4) as executor:
            roman_numerals = list(executor.map(convert_to_roman, numbers))

        # Build results
        results = [
            {'input': str(num), 'output': roman}
            for num, roman in zip(numbers, roman_numerals)
        ]

        return jsonify({'conversions': results})
    return jsonify({'error': 'Missing required parameters. Provide either "query" or both "min" and "max".'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)

# TODO: I'm not sure i'm even doing the right 400 responses, etc.
# TODO: add preferred method with different functions and urls per type of request
# TODO: add comments everywhere
# TODO: add logging
# TODO: add rate limiting
# TODO: add password?
# TODO: dockerize
# TODO: comment code
# TODO: explain everything in README
