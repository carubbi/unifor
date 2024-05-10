# Questão 3 (1 ponto)
# Implemente em Python, um algoritmo para calcular a média aritmética entre duas notas 
# de um aluno e mostrar sua situação, que pode ser aprovado ou reprovado.

def situacao_aluno():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))

    if nota1 >= 0 and nota2 >= 0:
        media = (nota1 + nota2) / 2
        if media >= 7:
            print("O aluno está aprovado!")
        else:
            print("O aluno está reprovado!")
    else:
        print("A nota deve ser maior que zero!")
