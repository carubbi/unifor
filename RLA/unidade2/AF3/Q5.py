# Questão 5 - Cálculo fatorial
# Dado um número n, implemente e teste um algoritmo para calcular o fatorial de n (escrito como n!), onde n ≥ 0.
# Obrigatório uso da estrutura composta try / except.

def calc_fatorial(n: int) -> None:
    """
    Calcula o fatorial de um número inteiro não-negativo e imprime o resultado.
    """
    if n >= 0:
        fatorial: int = 1

        for i in range(1, n + 1):
            fatorial *= i

        print(f"{n}! = {fatorial}")
    else:
        print("O valor deve ser maior ou igual a zero!")

def main() -> None:
    n: int = 5
    calc_fatorial(n)

if __name__ == "__main__":
    main()
