def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b


if __name__ == "__main__":
    print("Calculadora")
    print("40 + 2 =", sumar(40, 2))
    print("10 - 4 =", restar(10, 4))
    print("6 x 7 =", multiplicar(6, 7))
    print("9 / 3 =", dividir(9, 3))
