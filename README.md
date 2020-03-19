# SymbolicAbstraction
- ``core/`` holds base class definitions for abstract and concrete states as
  well as logic formulas.
- ``domains/`` holds definitions for particular abstract domains.
- ``algorithms/`` contains the algorithms acting on ``core/`` classes (ex.  RSY
  and bilateral).
- ``tests/`` holds PyTest unit tests.

# Running Tests
A docker container is provided to run tests.

```
make docker-test
```
