"""
Run pytest on the parent directory with PyCharm or command-line tool. 'run 'pytest' in ..'

All tests need to begin or end with: test
pytest is likely not the default test runner - unittest, built-in to python
"""
import pytest
from main.objects import polynomial


@pytest.fixture()  # fixtures are run once at the beginning
def poly_fixture():
    degrees = [1, 2, 3]  # 0 1 2 degree 1 + 2x + 3x^2
    poly = polynomial(degrees)
    return poly


def test_make_polynomial(poly_fixture):
    poly = poly_fixture
    assert poly.evaluate(0) == 1, 'p(0) is not 1'
    assert poly.evaluate(1) == 6, 'p(1) is not 6'
    assert pytest.approx(poly.evaluate(3.14), 36.8588), 'p(3.14) is not 36.8588'


def test_print_polynomial(poly_fixture):
    poly = poly_fixture
    assert poly.__str__() == '1x^0 + 2x^1 + 3x^2'
    print(poly)


def test_add_polynomial(poly_fixture):
    p1 = poly_fixture
    p2 = poly_fixture
    p3 = p1 + p2
    assert p3.coefs == [2, 4, 6], 'sum of coefficients is not correct'
    p4 = polynomial([1, 1, 1, 1])
    p5 = p4 + p1
    assert p5.coefs == [2, 3, 4, 1], 'sum of coefs with mixed degree is not correct'
    # test other try-except pattern
    p5 = p1 + p4
    assert p5.coefs == [2, 3, 4, 1], 'sum of coefs with mixed degree is not correct'
