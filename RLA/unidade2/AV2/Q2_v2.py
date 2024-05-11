def preencher_pontuacoes(n: int) -> list[int]:
    """
    Simula o preenchimento do vetor com as pontuações do jogador em cada partida,
    permitindo que o usuário insira manualmente as pontuações durante a execução
    do programa.
    """
    # Inicializa uma lista para armazenar as pontuações
    vec: list[int] = [0] * n

    # Simula o preenchimento dos vetores com as pontuações dos jogadores A e B
    for i in range(n): # 0,1,2,...,9
        vec[i] = int(input(f"Digite a pontuação na partida {i+1}: "))

    return vec

def revisar_pontuacao(vec, pos, valor):
    """Anula a pontuação na posição especificada"""
    vec[pos-1] = valor
    return vec

def diferenca_pontuacao(vec_a: list[int], vec_b: list[int]) -> list[int]:
    """
    Esta função calcula as diferenças entre as pontuações dos jogadores A e B
    nas respectivas partida.
    """
    # Inicializa lista para armazenar as diferenças
    n = len(vec_a)
    vec_dif = [0] * n

    # Calcula a diferença entre as pontuações e adicionar à lista
    for i in range(n): # 0,1,2,...,9
        vec_dif[i] = abs(vec_a[i] - vec_b[i])

    return vec_dif

def maior_diferenca(vec_a, vec_b):
    """
    Esta função percorre todas as combinações de pontuações possíveis entre os
    jogadores A e B e retorna a maior diferença absoluta entre elas.
    """
    # Inicializa variável para armazenar a maior diferença
    maior = 0

    # Itera sobre todas as pontuações para encontrar a maior diferença
    for pta in vec_a:
        for ptb in vec_b: # pta3,ptb2, pta3,ptb2, ..., pta3,ptbn (combinações possiveis)
            dif = abs(pta - ptb)
            # dif = pta - ptb
            # if dif < 0:
            #     dif = -dif
            if dif > maior:
                maior = dif

    return maior

def imprimir(vec, nome=None):
    if nome:
        print(f"{nome}:", end=" ")

    for k in vec:
        print(k, end= " ")
    print()

def main() -> None:
    # Preenchimento do vetor com as pontuações
    print("Entrada das pontuações do jogador A:")
    vec_a = preencher_pontuacoes(10)

    print("\nEntrada das pontuações do jogador B:")
    vec_b = preencher_pontuacoes(10)

    print("\nPontuações dos jogadores:")
    imprimir(vec_a, "A")
    imprimir(vec_b, "B")

    # Revisão das pontuações
    vec_a = revisar_pontuacao(vec_a, 10, 388)
    vec_b = revisar_pontuacao(vec_b, 8, 370)

    print("\nPontuações finais dos jogadores:")
    imprimir(vec_a, "A")
    imprimir(vec_b, "B")

    # Diferença entre as respectivas partidas
    vec_dif = diferenca_pontuacao(vec_a,vec_b)

    print("\nDiferenças entre as partidas (pontos):", end=" ")
    imprimir(vec_dif)

    # Diferença entre todas as combinações possíveis
    dif = maior_diferenca(vec_a, vec_b)
    print(f"\nMaior diferença entre todas as partidas: {dif} pontos")

if __name__ == "__main__":
    main()
