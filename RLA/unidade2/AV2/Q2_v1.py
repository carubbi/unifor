"""
Questão 02 (4 pontos)

Considere que você está desenvolvendo um programa para calcular e analisar as pontuações de dois jogadores, A e B, ao longo de uma série de partidas. 
As pontuações são armazenadas em vetores correspondentes aos jogadores, onde cada elemento do vetor representa a pontuação em uma partida específica.
"""

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

def revisar_pontuacao(vec: list[int], num_partida: int, valor: int):
    """Revisa a pontuação na posição especificada"""
    vec[num_partida-1] = valor
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
        dif = vec_a[i] - vec_b[i]
        vec_dif[i] = abs(dif)
        # if dif < 0:
        #     dif = -dif
        # vec_dif[i] = dif

    return vec_dif

def maior_diferenca(v: list[int]) -> int:
    maior: float = v[0]
    n = len(v)
    for i in range(1, n):
        if v[i] > maior:
            maior = v[i]
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

    # Revisão das pontuações T160-60 / T160-80
    vec_a = revisar_pontuacao(vec_a, 8, 388)
    vec_b = revisar_pontuacao(vec_b, 10, 370)

    print("\nPontuações finais dos jogadores (T160-60 / T160-80):")
    imprimir(vec_a, "A")
    imprimir(vec_b, "B")

    # Revisão das pontuações T160-39 / T998-31
    vec_a = revisar_pontuacao(vec_a, 10, 388)
    vec_b = revisar_pontuacao(vec_b, 8, 370)

    print("\nPontuações finais dos jogadores (T160-39 / T998-31):")
    imprimir(vec_a, "A")
    imprimir(vec_b, "B")

    # Diferença entre as respectivas partidas
    vec_dif = diferenca_pontuacao(vec_a,vec_b)

    print("\nDiferenças entre as partidas (pontos):", end=" ")
    imprimir(vec_dif)

    # Diferença entre todas as partidas
    maior_dif = maior_diferenca(vec_dif)
    print(f"\nMaior diferença entre todas as partidas: {maior_dif} pontos")

if __name__ == "__main__":
    main()
