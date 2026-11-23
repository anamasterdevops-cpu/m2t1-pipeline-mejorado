import pytest

from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(40, 2) == 42


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(6, 7) == 42


def test_dividir():
    assert dividir(9, 3) == 3


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
