## Solution testing

### 1. To test using unittest module

    python test_problem.py
    python -m unittest

### 2. To test using pytest

    python -m pytest test_problem

### 3. To run coverage and generate report

    coverage run test_problem
    coverage report -m

### Generated Report

    coverage report -m
    Name              Stmts   Miss  Cover   Missing
    -----------------------------------------------
    problem.py           13      0   100%
    test_problem.py      21      0   100%
    -----------------------------------------------
    TOTAL                34      0   100%
