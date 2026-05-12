# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

Learn how to write and run unit tests using pytest to verify that your Python functions work correctly. By the end of this assignment, you'll be able to write tests that catch bugs, document expected behavior, and give you confidence in your code.

## 📝 Tasks

### 🛠️ Task 1: Write Your First Unit Tests

#### Description
Write unit tests for the provided calculator module. Each test should verify that a function returns the correct result for a specific input. Start with simple cases (normal inputs) before testing edge cases.

#### Requirements
Your test file should:

- Import pytest and the calculator functions
- Write at least 3 test functions: one for `add()`, one for `subtract()`, and one for `multiply()`
- Use `assert` statements to verify the functions return expected results
- Run your tests with `pytest` and confirm they all pass

**Example:**
```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

---

### 🛠️ Task 2: Test Edge Cases and Error Conditions

#### Description
Expand your tests to include edge cases (boundary conditions, unusual inputs) and error handling. This is where real bugs hide!

#### Requirements
Your tests should:

- Test with zero, negative numbers, and large numbers
- Test division by zero (verify it raises an exception)
- Use `pytest.raises()` to check that errors are raised appropriately
- Write at least 2 additional test functions for edge cases
- All tests should pass

**Example:**
```python
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

### 🛠️ Task 3: Test a Pre-built Module (Stretch Goal)

#### Description
Write comprehensive tests for the `string_utils` module, which provides string manipulation functions. Think like a quality assurance engineer—what inputs might break this code?

#### Requirements
Your test file should:

- Write tests for at least 3 functions in `string_utils`
- Test normal cases, edge cases (empty strings, single characters), and special inputs (spaces, symbols)
- Achieve at least 80% code coverage (all major code paths tested)
- Document what each test is checking with a clear test name or comment
- All tests should pass

**Hint:** Run `pytest --cov` to see code coverage.
