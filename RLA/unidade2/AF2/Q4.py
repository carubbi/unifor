# Questão 4 (1 ponto)
# Elaborar um algoritmo que, dada a idade, classifique nas categorias: infantil A (5 - 7 anos), infantil B (8 -10 anos), juvenil A (11 - 13 anos), juvenil B (14 -17 anos) e adulto (maiores que 18 anos).

def classificar_categoria():
    idade = int(input("Digite a idade do aluno: "))

    if idade >= 5 and idade <= 7:
        print("Infantil A")
    elif idade >= 8 and idade <= 10:
        print("Infantil B")
    elif idade >= 11 and idade <= 13:
        print("Juvenil A")
    elif idade >= 14 and idade <= 17:
        print("Juvenil B")
    elif idade >= 18:
        print("Adulto")
    else:
        print("Digite uma idade válida!")

if __name__ == "__main__":
    classificar_categoria()
