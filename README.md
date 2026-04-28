# Python Utils & Testing

A small Python library of utility functions for list manipulation, with a full test suite demonstrating both `pytest` and `unittest` approaches and test coverage reporting.

## Features

- **`get(array, index, default=None)`** — safely retrieves an element by index; returns `default` if the index is out of range. Only works with non-negative indices.
- **`my_slice(coll, start=None, end=None)`** — returns a new list containing a portion of the original; supports negative indices as offsets from the end.

## Project Structure

```
python-tests/
├── utils/
│   └── arrs.py          # Utility functions
├── tests/
│   ├── test_arrs_pytest.py    # Tests using pytest
│   └── test_arrs_unittest.py  # Tests using unittest
└── requirements.txt
```

## Installation

Clone the repository and install dependencies:

```bash
git clone <repo-url>
cd python-tests
pip install -r requirements.txt
```

## Running Tests

**With pytest:**

```bash
pytest tests/ -v
```

**With unittest:**

```bash
python -m unittest discover tests/
```

**With coverage report:**

```bash
pytest tests/ --cov=utils --cov-report=term-missing
```

## Usage Examples

```python
from utils import arrs

# get — safe index access
arrs.get([10, 20, 30], 1)           # 20
arrs.get([10, 20, 30], 5)           # None
arrs.get([10, 20, 30], 5, "n/a")    # "n/a"

# my_slice — list slicing with optional bounds
arrs.my_slice([1, 2, 3, 4], 1, 3)   # [2, 3]
arrs.my_slice([1, 2, 3, 4], -2)     # [3, 4]
arrs.my_slice([1, 2, 3, 4])         # [1, 2, 3, 4]
```

## Tech Stack

- Python 3
- [pytest](https://docs.pytest.org/) — primary test runner
- [unittest](https://docs.python.org/3/library/unittest.html) — standard library test framework
- [pytest-cov](https://pytest-cov.readthedocs.io/) — test coverage
