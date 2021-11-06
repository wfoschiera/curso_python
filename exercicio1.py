"""
Crie uma função que some dois numeros
Crie outra função que multiplique dois numeros
"""
def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b


if __name__ == "__main__":
    assert soma(1, 2) == 3
    assert multiplicacao(2, 3) == 6
