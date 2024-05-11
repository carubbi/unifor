# Questão 1 - Troca dos valores de duas variáveis
# Dadas duas variáveis, $a$ e $b$, implemente e teste um algoritmo para trocar os valores atribuídos a elas.

def troca_valores(a:float, b: float) -> None:
    """
    Troca os valores atribuídos aos parâmetros a e b.
    """
    aux: float = a
    a = b
    b = aux

    print("a =", a)
    print("b =", b)

def main() -> None:
    a = -2
    b = 4
    troca_valores(a,b)

if __name__ == "__main__":
    main()
