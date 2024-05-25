"""
Questão 01 (4 pontos)

O rendimento acadêmico da UNIFOR é acompanhado por meio de três registros de Avaliação (AV1, AV2 e AV3), resultantes da consolidação do desempenho nas atividades avaliativas 
aplicadas em cada período e aferido por Nota Final (NF) correspondente à média aritmética entre a nota resultante da média de AV1 e AV2 e a nota de AV3, atribuídas numa escala 
de 0,0 a 10,0, conforme a seguinte fórmula:

$$NF = [(AV1 + AV2)/2 + AV3]/2$$

Estará aprovado por rendimento acadêmico, o aluno que obtiver Nota Final ($NF$) igual ou superior a $5,0$ (cinco vírgula zero), desde que a nota resultante da média entre 
$AV1$ e $AV2$ seja igual ou superior a $4,0$ (quatro vírgula zero) e a nota de $AV3$ seja igual ou superior a $4,0$ (quatro vírgula zero).

Entradas obrigatórias:

AV1: 8.5, AV2: 7.0, AV3: 9.0 (entrada solicitada)
AV1: 2.5, AV2: 5.5, AV3: 5.0 (entrada solicitada)
AV1: 9.5, AV2: 8.5, AV3: 3.0 (entrada solicitada)
AV1: 1.0, AV2: 6.0 (não solicita a nota da AV3)

Saídas esperadas:

Digite a nota da AV3: nove
Digite um valor válido!

Digite a nota da AV3: 9
Nota: 8.4 Aprovado!

Digite a nota da AV3: 5
Nota: 4.5 Reprovado

Digite a nota da AV3: 3
Nota: 6.0 Reprovado

Nota da AV3 não informada!
Nota 3.5 Reprovado
"""

def calcular_nota_final(av1, av2, av3):
    """
    Calcula a nota final de acordo com as av1, av2 e av3.
    """
    nfinal = ((av1 + av2) / 2 + av3) / 2
    return nfinal

def media_av1_av2(av1, av2):
    """
    Calcula a média parcial de acordo com as av1 e av2.
    """
    med = (av1 + av2) / 2
    return med

def situacao_aluno(av1, av2):
    """
    Exibe a nota final e a situação do aluno. 
    """
    media = media_av1_av2(av1, av2)
    if media >= 4.0:
        while True:
            try:
                av3 = float(input("Digite a nota da AV3: "))
                break
            except ValueError as e:
                # print(e)
                print("Digite um valor válido!\n")
        nf = calcular_nota_final(av1, av2, av3)
        if av3 >= 4 and nf >= 5.0:
            print(f"Nota: {nf:.1f} Aprovado!\n")
        else:
            print(f"Nota: {nf:.1f} Reprovado\n")
    else:
        print("Nota da AV3 não informada!")
        print(f"Nota {media:.1f} Reprovado\n")

def main():

    # Caso 1
    av1 = 8.5
    av2 = 7.0
    situacao_aluno(av1, av2)

    # Caso 2
    av1 = 2.5
    av2 = 5.5
    situacao_aluno(av1, av2)

    # Caso 3
    av1 = 9.5
    av2 = 8.5
    situacao_aluno(av1, av2)

    # Caso 4
    av1 = 1.0
    av2 = 6.0
    situacao_aluno(av1, av2)

if __name__ == "__main__":
    main()
