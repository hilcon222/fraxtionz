from fraxtionz import Rational


def test_true():
    assert True


def test_init():
    f = Rational(1, 2)
    assert f.n == 1
    assert f.d == 2


def test_zerodivisionerror():
    try:
        f = Rational(1, 0) # noqa
    except ZeroDivisionError:
        pass
    else:
        raise RuntimeError("ZeroDivisionError doesn't raise when the denominator is equal to 0.") # noqa


def test_reduction():
    f = Rational(2, 6)
    assert f.n == 1
    assert f.d == 3


def test_lcm():
    assert Rational.lcm(10, 15) == 30


def test_lcden():
    assert Rational(1, 10).lcden(Rational(1, 15)) == 30


def test_add():
    assert Rational(1, 2) + Rational(2, 4) == Rational(4, 4)
    assert Rational(4, 4) + 1 == Rational(2, 1)


def test_lt():
    assert Rational(1, 3) < Rational(1, 2)


def test_eq():
    assert Rational(1, 1) == Rational(1, 1)


def test_gt():
    assert Rational(8, 4) > Rational(4, 8)


def test_invert():
    assert Rational(3, 4).__invert__() == Rational(4, 3)


def test_truediv():
    assert Rational(4, 6) / Rational(4, 6) == Rational(1, 1)
    assert Rational(4, 1) / Rational(2, 1) == Rational(2, 1)
    assert 4 / Rational(2) == Rational(2)


def test_floordiv():
    assert Rational(2) // Rational(2) == 1
    assert 4 // Rational(4, 2) == 2


def test_sub():
    assert Rational(4, 2) - Rational(1, 1) == Rational(1, 1)


def test_floatdump():
    assert round(Rational(1, 3).floatdump(), 1) == 0.3


def test_floatofract():
    assert Rational.floatofract(0.3) == Rational(3, 10)


def test_pow():
    assert Rational(3, 4) ** 3 == Rational(27, 64)
    assert Rational(2, 3) ** -3 == Rational(27, 8)
