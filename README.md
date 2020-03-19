# SymbolicAbstraction
- ``core/`` holds base class definitions for abstract and concrete states as
  well as logic formulas.
- ``domains/`` holds definitions for particular abstract domains.
- ``algorithms/`` contains the algorithms acting on ``core/`` classes
  (currently RSY and bilateral algorithms for symbolic abstraction).
- ``frontend/`` contains a simple two-operand language for which abstract
  transformers can be automatically derived via the symbolic abstraction
  algorithms.
- ``tests/`` holds PyTest unit tests.

# Running Tests
A docker container is provided to run tests, which can be executed by the
following `make` rule:
```
make docker-test
```

Alternatively, if you have an up-to-date version of Python 3 and Pytest
installed you can run
```
python3 -m pytest tests
```

# Examples
## Test Cases
The test cases in `tests/` demonstrate usage of most of the individual
functionality.

## Entire Example Program
An example program is available in `example_program.py` which demonstrates how
Symbolic Abstraction can be used to automatically compute an abstract
transformer for a straight-line program.

## Reduced Product
The test case in `tests/test_reduced_product_domain/test_reduce.py` shows how
Symbolic Abstraction can be used to automatically compute the reduced product
of two abstract domains.

# People
Code written by Matthew Sotoudeh (contact
[masotoudeh@ucdavis.edu](mailto:masotoudeh@ucdavis.edu)), advised and reviewed
by Professor Aditya Thakur (contact
[avthakur@ucdavis.edu](mailto:avthakur@ucdavis.edu)). For more information,
please see the [Davis Automated Reasoning Group](http://darg.cs.ucdavis.edu/).

# Papers, Citation
The algorithms used here are adapted from:
```
Thakur, A. V. (2014, August). Symbolic Abstraction: Algorithms and Applications
(Ph.D. dissertation). Computer Sciences Department, University of Wisconsin,
Madison.
```
The dissertation is available
[here](http://thakur.cs.ucdavis.edu/bibliography/thakur_PHD14.html).

To cite the dissertation, please use the following bibtex:
```
@phdthesis{thakur_PHD14,
    author = {Thakur, Aditya V.},
    title = {Symbolic Abstraction: Algorithms and Applications},
    school = {Computer Sciences Department, University of Wisconsin, Madison},
    type = {Ph.D. dissertation},
    month = aug,
    year = {2014}
}
```
