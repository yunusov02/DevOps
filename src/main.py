def add(a: int, b: int):
    return a + b

def substraction(a: int, b: int):
    return a - b


def multiplication(a: int, b: int):
    return a * b


def division(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError
    return a / b

