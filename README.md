# brent_test
### Overview
- API that converts arabic numbers to roman numerals, range 1:3999
- API also accepts ranges in the form of `min=1&max=100`
- Multithreaded
- Dockerized
- Contains monitoring, logging, and reporting. (Prometheus, Grafana)
### Sources
- Used an [online calculator](https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php) to help make my test cases.
- Wikipedia page on [roman numerals](https://en.wikipedia.org/wiki/Roman_numerals)
### Tech Stack:
- Python 3.12
- Flask
- Unittest
- Logging
- Prometheus
- Grafana
### Methodology:
- 
### Building and Running:
- 
### Preferred Solution:
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
