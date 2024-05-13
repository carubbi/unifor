# Questão 4
# Implemente em Python, um algoritmo que, a partir da idade do candidato(a), 
# determinar se pode ou não tirar a CNH. Caso não atender a restrição de idade, 
# calcular quantos anos faltam para o candidato estar apto.

def verificar_apto_cnh():
    idade = int(input("Digite a sua idade: "))

    if idade < 0:
        print("A idade deve ser maior que zero!")
    else:
        if idade >= 18:
            print("O candidato está apto a tirar a CNH!")
        else:
            anos_apto = 18 - idade
            print(f"Faltam {anos_apto} ano(s) para o candidato estar apto!")
