import calc
import pytest


@pytest.mark.number
def test_add():
    assert calc.add(2, 5) == 7
    assert calc.add(0) == 2
    assert calc.add(-2, 5) == 3


@pytest.mark.number
def test_multiply():
    assert calc.multiply(2, 5) == 10
    assert calc.multiply(-2) == -8
    assert calc.multiply(0, 0) == 0


@pytest.mark.strings
def test_add_strings():
    result = calc.add("Hello", " World")
    assert result == 'Hello World'
    assert type(result) is str


@pytest.mark.strings
def test_multiply_strings():
    assert calc.multiply("Hello ", 2) == 'Hello Hello '
    result = calc.multiply("Ziom")
    assert type(result) is str
    assert result == "ZiomZiomZiomZiom"
