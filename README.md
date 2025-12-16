# brent_test
### Sources
- Used an online calculator to help make my test cases [link](https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php)
- Wikipedia page on [roman numerals](https://en.wikipedia.org/wiki/Roman_numerals)
### Methodology
### Preferred Solution
- According to the spec the solution needs a single endpoint that can determine whether the request is for a single number (query) or a range of numbers (min & max)
- My solution to this is a single function with a big if..else statement to determine which parameters have been used.
- I think it would be better to separate these endpoints into different units, making development and testing easier.
- Example: an endpoint like `romannumeral/query` and a second one called `romannumeral/range`
- Then my project structure could have separate folders per endpoint and separate test files per endpoint.

### Towards Production:
- As the project gets closer to production there are three things I would implement:
    1. Rate Limiting
        - Using flask_limiter library
    2. Auth
        - Require a token in each request
    3. Kubernetes
        - autoscaling
        - rolling updates
        - self healing