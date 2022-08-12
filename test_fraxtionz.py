from fraxtionz import Fraction


def test_true():
    assert True


def test_init():
    f = Fraction(1, 2)
    assert f.n == 1
    assert f.d == 2


def test_zerodivisionerror():
    try:
        f = Fraction(1, 0) # noqa
    except ZeroDivisionError:
        pass
    else:
        raise RuntimeError("ZeroDivisionError doesn't raise when the denominator is equal to 0.") # noqa


def test_reduction():
    f = Fraction(2, 6)
    assert f.n == 1
    assert f.d == 3


def test_lcm():
    assert Fraction.lcm(10, 15) == 30


def test_lcden():
    assert Fraction(1, 10).lcden(Fraction(1, 15)) == 30


def test_add():
    assert Fraction(1, 2) + Fraction(2, 4) == Fraction(4, 4)
    assert Fraction(4, 4) + 1 == Fraction(2, 1)


def test_lt():
    assert Fraction(1, 3) < Fraction(1, 2)


def test_eq():
    assert Fraction(1, 1) == Fraction(1, 1)


def test_gt():
    assert Fraction(8, 4) > Fraction(4, 8)


def test_invert():
    assert Fraction(3, 4).__invert__() == Fraction(4, 3)


def test_truediv():
    assert Fraction(4, 6) / Fraction(4, 6) == Fraction(1, 1)
    assert Fraction(4, 1) / Fraction(2, 1) == Fraction(2, 1)
    assert 4 / Fraction(2) == Fraction(2)


def test_floordiv():
    assert Fraction(2) // Fraction(2) == 1
    assert 4 // Fraction(4, 2) == 2


def test_sub():
    assert Fraction(4, 2) - Fraction(1, 1) == Fraction(1, 1)


def test_floatdump():
    assert round(Fraction(1, 3).floatdump(), 1) == 0.3


def test_floatofract():
    assert Fraction.floatofract(0.3) == Fraction(3, 10)
