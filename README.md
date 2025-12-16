# brent_test
### Overview
- API that converts arabic numbers to roman numerals, range 1:3999
- API also accepts ranges in the form of `min=1&max=100`
- Multithreaded
- Dockerized
- Contains monitoring, logging, and reporting. (Prometheus, Grafana)
### Sources
- Used an [online calculator](https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php) to help make my test cases and think through my conversion algorithm.
- Wikipedia page on [roman numerals](https://en.wikipedia.org/wiki/Roman_numerals)
### Tech Stack:
- Python 3.12
- Flask
- Unittest
- Logging
- Prometheus
- Grafana
### Methodology:
1. **Algorithm Design**: Created a greedy algorithm using a dictionary of Roman numeral values (largest to smallest). For each input number, subtract the largest possible Roman value and append the corresponding numeral until the number reaches zero.

2. **API Design**: Built a single Flask endpoint that handles both single conversions (`query` parameter) and range conversions (`min` & `max` parameters) through conditional logic.

3. **Parallel Processing**: Implemented `ProcessPoolExecutor` for range requests to convert multiple numbers concurrently, improving performance for large ranges.

4. **Testing**: Used `unittest` framework with comprehensive test cases covering edge cases, invalid inputs, and range requests.

5. **Monitoring**: Integrated Prometheus metrics to track API request counts, latency, and error rates. Grafana provides visualization dashboards.

6. **Containerization**: Dockerized the Flask app alongside Prometheus and Grafana using Docker Compose for easy deployment and orchestration.

### Building and Running:

**Prerequisites:**
- Docker Desktop installed and running
- Python 3.12+ (for local development)

**Using Docker:**
```bash
# Clone the repository
git clone https://github.com/standley-brent/brent_test.git
cd brent_test

# Start all services (Flask, Prometheus, Grafana)
docker compose up --build

# API available at: http://localhost:5001
# Prometheus at: http://localhost:9090
# Grafana at: http://localhost:3000 (admin/admin)
```

**Local Development:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python converter.py

# Run tests
python -m unittest discover tests
```

**Example API Requests:**
```bash
# Single conversion
curl "http://localhost:5001/romannumeral/?query=42"

# Range conversion
curl "http://localhost:5001/romannumeral/?min=1&max=10"
```

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
