# is-odd

[![PyPI version](https://badge.fury.io/py/is-odd.svg)](https://badge.fury.io/py/is-odd)

Why determine if something is odd or odd the usual way when you can do it with ✨AI✨?

Our library has 100% test coverage!

`is-odd` is a Python library that uses OpenAI's GPT-4o-mini model to tell if a number is even or odd. Add some AI magic to your number-checking tasks!

## Installation

To install `is-odd`, use pip:

```bash
pip install is-odd
```

## SetupTo use is-odd, you’ll need an OpenAI API key. Get one by signing up at OpenAI.

1. Create a .env file in the root of your project.
2. Add your OpenAI API key to the .env file:

```
OPENAI_API_KEY=your-api-key
```
Replace `your-api-key` with your actual OpenAI API key.

## Usage
Here’s an example of how to use the `is-odd` package in your project:

```
from is_odd import is_odd

# Example usage
number = 5
result = is_odd(number)
print(f"Is {number} odd? {result}")  # Output: Is 5 odd? True
```

## Function
`is_odd(number)`
- Parameters: `number` (int) - The number to check.
- Returns: `bool` - `True` if the number is odd, `False` if even.
- Raises: `ValueError` if the API response is inconclusive or if there's an issue with the request.


## Running Tests
To test the `is_event` library, use the unittest framework:


```bash
python -m unittest discover -s tests
```

## Generating a Coverage Report
To check code coverage, make sure you have coverage installed:

```bash
pip install coverage
```
Run tests with coverage enabled:
```bash
coverage run -m unittest discover -s tests
```

To see a summary report in the terminal, use:
```bash
coverage report
```

To create a detailed HTML report:
```bash
coverage html
```

Open `htmlcov/index.html` in your browser to view the line-by-line coverage details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the Apache 2.0 license.
