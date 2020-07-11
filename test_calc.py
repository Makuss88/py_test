import calc


def test_add():
    assert calc.add(2, 5) == 7
    assert calc.add(0) == 2
    assert calc.add(-2, 5) == 3


def test_multiply():
    assert calc.multiply(2, 5) == 10
    assert calc.multiply(-2) == -8
    assert calc.multiply(0, 0) == 0


def test_add_string():
    result = calc.add("Hello", " World")
    assert result == 'Hello World'
    assert type(result) is str


def test_multiply_string():
    assert calc.multiply("Hello ", 2) == 'Hello Hello '
    result = calc.multiply("Ziom")
    assert type(result) is str
    assert result == "ZiomZiomZiomZiom"
