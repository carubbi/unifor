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

# Questão 8: Jogo de Adivinhação com múltiplas tentativas
# Descrição geral do algoritmo

from random import randint

def jogo_adivinhacao(inicio: int, fim: int, n:int) -> None:

    # Condições de execução (não obrigatório)
    assert isinstance(inicio, int), "Valor de início deve ser inteiro!"
    assert isinstance(fim, int), "Valor de fim deve ser inteiro!"
    assert fim > inicio, "O valor de fim deve ser maior que o valor de início!"


    # Mensagen iniciais
    print(f"Tente adivinhar o número entre {inicio} e {fim}.")
    print(f"Você tem {n} tentativas!")

    # Gera um número inteiro aleatório
    num: int = randint(inicio, fim)
    print(f"Número secreto para testar o código: {num}")


    # Inicializa o número de tentativas
    cont: int = 1

    # Loop para gerar o jogo
    while cont <= n:

        print(f"\n\tTentativa número {cont}")

        try:
            chute: int = int(input("\tChute um número: "))
        except ValueError as e:
            print("\tOps! Digite um valor válido ...")
            print(f"\tMensagem de erro: {e}")
            continue

        if chute < num:
            print("\tChute muito baixo!")
        elif chute > num:
            print("\tChute muito alto!")
        else:
            print(f"\nParabéns! Você acertou o número {num}!")
            break

        cont+= 1

    if chute != num:
        print(f"\nVocê gastou suas {cont-1} tentativas!!! O número era {num}.")

    print(f"Fim de jogo!")

def main() -> None:
    inicio: int = 0
    fim: int = 10
    n: int = 3
    jogo_adivinhacao(inicio, fim, n)

if __name__ == "__main__":
    main()
