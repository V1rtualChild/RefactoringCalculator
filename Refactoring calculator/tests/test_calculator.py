import pytest
import sys
import os
from pathlib import Path

# Додаємо шлях до папки проекту
sys.path.append(str(Path(__file__).parent.parent))

from refactored_code.calculator_refactored import Calculator
from refactored_code.operations import Addition, Subtraction, Multiplication, Division

# Тести для базових операцій
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5), (-1, 1, 0), (0, 0, 0), (999, 1, 1000)
])
def test_addition(a, b, expected):
    assert Addition().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2), (10, -5, 15), (0, 0, 0), (-3, -2, -1)
])
def test_subtraction(a, b, expected):
    assert Subtraction().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12), (-2, 5, -10), (0, 100, 0), (-3, -3, 9)
])
def test_multiplication(a, b, expected):
    assert Multiplication().execute(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5), (-9, 3, -3), (5, 0.5, 10)
])
def test_division(a, b, expected):
    assert Division().execute(a, b) == expected

def test_division_by_zero():
    with pytest.raises(ValueError, match="Ділення на нуль!"):
        Division().execute(5, 0)

# Тести для Calculator
@pytest.fixture
def calculator():
    config_path = os.path.join(Path(__file__).parent.parent, "refactored_code", "config.json")
    return Calculator(config_path)

def test_calculator_operations(calculator):
    assert '+' in calculator.operations
    assert '-' in calculator.operations
    assert '*' in calculator.operations
    assert '/' in calculator.operations

def test_invalid_operator(calculator):
    with pytest.raises(KeyError):
        calculator.operations["%"]

def test_config_loading(calculator):
    assert calculator.config["limits"]["max_input"] == 1000

def test_default_config():
    calc = Calculator("non_existent_config.json")
    assert calc.config["limits"]["max_input"] == 1000