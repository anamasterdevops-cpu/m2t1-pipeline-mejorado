"""Calculadora sencilla que recibe sus datos por variables de entorno.

Tarea 1 - Módulo 2 - Máster DevSecOps (Ana).
Es la calculadora de la Tarea 2, reorganizada en funciones para poder probarla con pytest.
"""

import os
import sys

# Operaciones que admite la calculadora
OPERACIONES_VALIDAS = ("suma", "resta", "multiplicacion", "division", "potencia")


def sumar(a, b):
    """Devuelve a + b."""
    return a - b  # FALLO A PROPÓSITO: resta en vez de sumar


def restar(a, b):
    """Devuelve a - b."""
    return a - b


def multiplicar(a, b):
    """Devuelve a * b."""
    return a * b


def dividir(a, b):
    """Devuelve a / b. Si b es 0 lanza un error controlado (ValueError)."""
    if b == 0:
        raise ValueError("no se puede dividir entre cero")
    return a / b


def potencia(a, b):
    """Devuelve a elevado a b."""
    return a ** b


def calcular(operacion, a, b):
    """Elige la operación por su nombre y devuelve el resultado.

    Lanza ValueError si la operación no existe.
    """
    operacion = operacion.lower()
    if operacion == "suma":
        return sumar(a, b)
    if operacion == "resta":
        return restar(a, b)
    if operacion == "multiplicacion":
        return multiplicar(a, b)
    if operacion == "division":
        return dividir(a, b)
    if operacion == "potencia":
        return potencia(a, b)
    raise ValueError(f"operación no válida: {operacion}. Usa: {', '.join(OPERACIONES_VALIDAS)}")


def leer_numero(nombre):
    """Lee una variable de entorno y la convierte a número.

    Las variables de entorno siempre son texto. Si no es un número, lanza ValueError.
    """
    texto = os.environ.get(nombre, "0")
    try:
        return float(texto)
    except ValueError:
        raise ValueError(f"{nombre} debe ser un número (recibido: {texto})") from None


def main():
    """Lee OPERACION, NUM1 y NUM2 del entorno, calcula e imprime el resultado.

    Devuelve 0 si todo va bien y 1 si hay un error (es el código de salida del programa).
    """
    operacion = os.environ.get("OPERACION", "suma")
    try:
        num1 = leer_numero("NUM1")
        num2 = leer_numero("NUM2")
        resultado = calcular(operacion, num1, num2)
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print("=== Calculadora en Docker ===")
    print(f"Operación: {operacion} | NUM1 = {num1:g} | NUM2 = {num2:g}")
    # :g quita los decimales innecesarios (42.0 se muestra como 42)
    print(f"Resultado: {resultado:g}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
