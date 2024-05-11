# Questão 3
# Escreva um programa que leia a nota de diversos alunos, até que seja digitada uma nota negativa.
# Nesse momento, ele mostra a média aritmética de todas as notas lidas e quantas notas foram lidas.
# Ex. Foram lidas 14 notas. A média aritmética é 6.75!

def quant_media():
    print("Digite a nota do aluno (nota negativa finaliza): ")
    nota = float(input())
    soma = 0
    cont = 0

    while nota >= 0:
        soma += nota
        cont += 1
        nota = float(input())

    if cont > 0:
        media = soma / cont
        print(f"Foram lidas {cont} nota(s). A média aritmética é {media:.1f}")

if __name__ == "__main__":
    quant_media()
