from calculator import calculator
import pytest


@pytest.mark.parametrize("operation, expected_result", [
    ("+", 6),
    ("-", 0),
    ("*", 9),
    ("/", 1)
])
def test_calculator_1(operation, expected_result):
    assert calculator(3, 3, operation) == expected_result
