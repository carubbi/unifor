# Questão 2
# Faça um algoritmo que exiba na tela uma contagem de 0 até n, exibindo apenas os múltiplos de 3.

def multiplo_tres():
    n = int(input("Digite a quantidade de números: "))
    for i in range(0, n + 1, 3):
        print(i, end=" ")

if __name__ == "__main__":
    multiplo_tres()
