# Questão 7 - Inversão dos dígitos de um número inteiro (2 pontos)
# Implemente e teste um algoritmo para inverter a ordem dos dígitos de um número inteiro positivo.<br> **Obrigatório uso da estrutura composta `try except`**.

def inverte_inteiro(num: int) -> None:
    """
    Inverte um número inteiro positivo e imprime o resultado.
    """
    if num < 0:
        print("O número deve ser positivo!")
    else:
        num_inv: int = 0

        while num > 0:
            digito: int = num % 10
            num_inv = (num_inv * 10) + digito
            num //= 10

        print("Número invertido:", num_inv)

def main() -> None:
    num: int = 537
    inverte_inteiro(num)

if __name__ == "__main__":
    main()
