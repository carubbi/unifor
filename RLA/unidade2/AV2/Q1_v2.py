"""
Questão 01
Desenvolva um programa para um jogo de adivinhação. O programa deve gerar aleatoriamente um número inteiro entre um valor mínimo e máximo definidos pelo usuário. 
O jogador terá um número limitado de tentativas para adivinhar o número gerado pelo programa. Após cada tentativa do jogador, o programa deve informar se o número 
número fornecido pelo jogador está perto ou distante do número aleatório, baseado nas condições: muito frio (dif<2), frio, quente e muito quente. O jogo continuará até que o jogador adivinhe corretamente o número aleatório ou esgote todas as tentativas.
"""
from random import randint

def jogo_adivinhacao(inicio: int, fim: int, n:int) -> None:

    # Condições de execução (opcional)
    assert isinstance(inicio, int), "Valor de início dado deve ser inteiro!"
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

        dif = abs(chute - num)
        # dif = chute - num
        # if dif < 0:
        #     dif = -1 * dif

        if dif == 0:
            print(f"\nParabéns! Você acertou o número {num}!")
            break
        elif dif < 2:
            print("\tEstá muito quente!")
        elif dif < 4:
            print("\tEstá quente!")
        elif dif < 6:
            print("\tEstá frio!")
        else:
            print("\tEstá muito frio!")

        cont+= 1

    if chute != num:
        print(f"\nVocê gastou suas {cont-1} tentativas!!! O número era {num}.")

    print(f"Fim de jogo!")

def main() -> None:
    inicio = 0
    fim = 10
    n = 3
    jogo_adivinhacao(inicio, fim, n)

if __name__ == "__main__":
    main()
