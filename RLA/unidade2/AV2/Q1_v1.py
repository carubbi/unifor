"""
Questão 01 (6 pontos)

Desenvolva um programa para um jogo de adivinhação. O programa deve gerar aleatoriamente um número inteiro entre um valor mínimo e máximo definidos pelo usuário. O jogador terá um número limitado de tentativas para adivinhar o número gerado pelo programa. Após cada tentativa do jogador, o programa deve informar se o número número fornecido pelo jogador é maior ou menor ao número aleatório. O jogo continuará até que o jogador adivinhe corretamente o número aleatório ou esgote todas as tentativas.
"""
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
