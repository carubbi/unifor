# Questão 1
# Implemente em Python, um algoritmo para determinar se um número inteiro e positivo é par ou impar.

def verifica_par_impar():
    numero = int(input("Digite um número: "))

    if numero >= 0:
        resto = numero % 2
        if resto == 0:
            print("O número é par!")
        else:
            print("O número é ímpar!")
    else:
        print("O número deve ser positivo!")

if __name__ == "__main__":
    verifica_par_impar()
