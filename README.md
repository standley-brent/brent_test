# brent_test
### Sources
### Methodology
### Preferred Solution
- According to the spec the solution needs a single endpoint that can determine whether the request is for a single number (query) or a range of numbers (min & max)
- My solution to this is a single function with a big if..else statement to determine which parameters have been used.
- I think it would be better to separate these endpoints into different units, making development and testing easier.
- Example: an endpoint like `romannumeral/query` and a second one called `romannumeral/range`
- Then my project structure could have separate folders per endpoint and separate test files per endpoint.