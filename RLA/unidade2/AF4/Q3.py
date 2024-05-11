# Questão 3 - Soma de um conjunto de números
# Dado um conjunto de $n$ números, implemente e teste um algoritmo para calcular a soma desses números. <br>
# Aceite apenas $n$ maior ou igual a zero.

def soma_numeros(n: int) -> None:
    """
    Calcula a soma de uma sequência de números.
    """
    if n >= 0:
        soma: int = 0
        i: int = 1

        while i <= n:
            num: int = int(input("Digite um número: "))
            soma += num
            i += 1

        print("A soma dos números é:", soma)
    else:
        print("O valor deve ser maior ou igual a zero!")

def main() -> None:
    n = 3
    soma_numeros(n)

if __name__ == "__main__":
    main()
