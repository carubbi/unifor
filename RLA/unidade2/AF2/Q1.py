# Questão 1
# Calcule a média de quatro números inteiros dados.

def calcular_media():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    num3 = float(input("Digite o número 3: "))
    num4 = float(input("Digite o número 4: "))

    media = (num1 + num2 + num3 + num4) / 4
    print(f"A média é {media:.1f}")

if __name__ == "__main__":
    calcular_media()
