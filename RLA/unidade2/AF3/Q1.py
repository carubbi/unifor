# Questão 1
# Atualize o algoritmo para determinar se um número inteiro e positivo é par ou ímpar, usando uma laço condicional para aceitar apenas números maiores ou iguais a zero.

def verifica_par_impar():
    num = -1
    while num < 0:
        num = int(input("Digite um número maior ou igual a zero: "))

    resto = num % 2
    if resto == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")

if __name__ == "__main__":
    verifica_par_impar()
