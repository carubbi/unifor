"""
O rendimento acadêmico da UNIFOR é acompanhado por meio de três registros de Avaliação (AV1, AV2 e AV3), 
resultantes da consolidação do desempenho nas atividades avaliativas aplicadas em cada período e aferido por Nota Final (NF) 
correspondente à média aritmética entre a nota resultante da média de AV1 e AV2 e a nota de AV3, atribuídas numa escala de 0,0 a 10,0, 
conforme a seguinte fórmula:

NF = [(AV1 + AV2)/2 + AV3]/2

Estará aprovado por rendimento acadêmico, o aluno que obtiver Nota Final (NF) igual ou superior a 5,0 (cinco vírgula zero), 
desde que a nota resultante da média entre AV1 e AV2 seja igual ou superior a 4,0 (quatro vírgula zero) e a nota de AV3 seja 
igual ou superior a 4,0 (quatro vírgula zero).
"""
def calcular_nota_final(av1, av2, av3):
    return ((av1 + av2) / 2 + av3) / 2

def media_av1_av2(av1, av2):
    return (av1 + av2) / 2

def situacao_aluno(av1, av2):
    media = media_av1_av2(av1, av2)
    if media >= 4.0:
        av3 = float(input("Digite a nota da AV3: "))
        nf = calcular_nota_final(av1, av2, av3)

        if nf >= 5.0:
            print(f"Nota: {nf:.1f} Aprovado!")
        else:
            print(f"Nota: {nf:.1f} Reprovado")
    else:
        med = (av1+av2)/2
        print(f"Nota {med:.1f} Reprovado")

def main():

    av1 = 8.5
    av2 = 7.0
    situacao_aluno(av1, av2)

    av1 = 2.5
    av2 = 5.5
    situacao_aluno(av1, av2)

    av1 = 1.0
    av2 = 6.0
    situacao_aluno(av1, av2)

if __name__ == "__main__":
    main()
