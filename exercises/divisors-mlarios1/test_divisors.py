from divisors import divisors


def test_one():
    assert divisors(1) == [1]


def test_two():
    assert divisors(2) == [1, 2]


def test_three():
    assert divisors(3) == [1, 3]


def test_twelve():
    assert divisors(12) == [1, 2, 3, 4, 6, 12]
