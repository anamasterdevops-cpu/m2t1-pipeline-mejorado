"""Pruebas unitarias de la calculadora con pytest."""

import pytest

import calculadora


# --- Un test por operación ---

def test_sumar():
    assert calculadora.sumar(40, 2) == 42


def test_restar():
    assert calculadora.restar(50, 8) == 42


def test_multiplicar():
    assert calculadora.multiplicar(6, 7) == 42


def test_dividir():
    assert calculadora.dividir(84, 2) == 42


def test_potencia():
    assert calculadora.potencia(2, 10) == 1024


# --- Casos de error ---

def test_dividir_entre_cero_lanza_error():
    with pytest.raises(ValueError, match="dividir entre cero"):
        calculadora.dividir(1, 0)


def test_operacion_no_valida_lanza_error():
    with pytest.raises(ValueError, match="operación no válida"):
        calculadora.calcular("raiz", 4, 2)


def test_numero_no_valido(monkeypatch):
    monkeypatch.setenv("NUM1", "hola")
    with pytest.raises(ValueError, match="NUM1 debe ser un número"):
        calculadora.leer_numero("NUM1")


# --- Test parametrizado: la misma prueba con varios datos ---

@pytest.mark.parametrize(
    "operacion, a, b, esperado",
    [
        ("suma", 1, 2, 3),
        ("resta", 5, 3, 2),
        ("multiplicacion", 3, 4, 12),
        ("division", 9, 3, 3),
        ("potencia", 3, 2, 9),
        ("SUMA", 1, 1, 2),  # también acepta mayúsculas
    ],
)
def test_calcular(operacion, a, b, esperado):
    assert calculadora.calcular(operacion, a, b) == esperado


# --- Pruebas de main() con variables de entorno (monkeypatch) ---

def test_main_suma(monkeypatch, capsys):
    monkeypatch.setenv("OPERACION", "suma")
    monkeypatch.setenv("NUM1", "40")
    monkeypatch.setenv("NUM2", "2")
    assert calculadora.main() == 0
    assert "Resultado: 42" in capsys.readouterr().out


def test_main_con_error(monkeypatch, capsys):
    monkeypatch.setenv("OPERACION", "division")
    monkeypatch.setenv("NUM1", "1")
    monkeypatch.setenv("NUM2", "0")
    assert calculadora.main() == 1
    assert "Error: no se puede dividir entre cero" in capsys.readouterr().out
