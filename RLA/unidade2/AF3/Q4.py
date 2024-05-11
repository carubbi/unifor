# Questão 4
# Dada uma sequência de números inteiros, calcular a sua soma.
# Por exemplo, para a sequência {12, 17, 4, -6, 8, 0}, o seu programa deve escrever o número 35.

def soma_valores():
    n = int(input("Digite a quantidade de números: "))
    soma = 0
    i = 1

    while i <= n:
        num = float(input(f"Digite o número {i}: "))
        soma += num
        i += 1

    print("A soma dos números é", soma)

if __name__ == "__main__":
    soma_valores()
