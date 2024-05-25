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
