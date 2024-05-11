"""
Questão 02 (4 pontos)

Considere que você está desenvolvendo um programa para calcular e analisar as notas de cinco (5) alunos matriculados 
nas disciplinas de Raciocínio Lógico Algorítimico (RLA) e Matemática para Computação (MAT). As notas são armazenadas 
em vetores correspondentes aos alunos, onde cada elemento do vetor representa a nota de um determinado aluno.
"""
def preencher_notas(n: int) -> list[int]:
    """
    Simula o preenchimento do vetor com as notas dos alunos em cada disicplina,
    permitindo que o usuário insira manualmente as notas durante a execução
    do programa.
    """
    # Inicializa uma lista para armazenar as pontuações
    vec: list[int] = [0] * n

    # Simula o preenchimento dos vetores com as pontuações dos jogadores A e B
    for i in range(n):
        vec[i] = float(input(f"Digite a nota do aluno {i+1}: "))

    return vec

def contar_aprovados(notas: list[int]) -> int:
    cont: int = 0
    for nota in notas:
        if nota >= 5 and nota <= 10:
            cont += 1
    return cont

def diferenca_pontuacao(vec_a: list[int], vec_b: list[int]) -> list[int]:
    """
    Esta função calcula as diferenças entre as notas dos alunos
    nas respectivas partida.
    """
    # Inicializa lista para armazenar as diferenças
    n = len(vec_a)
    vec_dif = [0] * n

    # Calcula a diferença entre as pontuações e adicionar à lista
    for i in range(n):
        dif = vec_a[i] - vec_b[i]
        vec_dif[i] = abs(dif)

    return vec_dif

def maior_diferenca(v: list[float]) -> float:
    idx = 0
    maior: float = v[idx]
    n = len(v)
    for i in range(1, n):
        if v[i] > maior:
            maior = v[i]
            idx = i
    return idx

def imprimir(vec, nome=None):
    if nome:
        print(f"{nome}:", end=" ")

    for k in vec:
        print(k, end= " ")
    print()

def main() -> None:
    # Preenchimento do vetor com as pontuações
    print("Entrada das notas de RLA:")
    n_alunos = 5
    vec_rla = preencher_notas(n_alunos)

    print("\nEntrada das notas de MAT:")
    vec_mat = preencher_notas(n_alunos)

    print("\nNotas dos alunos nas disciplinas:")
    imprimir(vec_rla, "RLA")
    imprimir(vec_mat, "MAT")

    # Contagem dos alunos aprovados por disciplina
    rla_aprov = contar_aprovados(vec_rla)
    mat_aprov = contar_aprovados(vec_mat)
    print(f"\nAprovados RLA: {rla_aprov} alunos")
    print(f"Aprovador MAT: {mat_aprov} alunos")

    # Diferença entre as respectivas disicplinas
    vec_dif = diferenca_pontuacao(vec_rla,vec_mat)

    print("\nDiferenças entre as disciplinas:", end=" ")
    imprimir(vec_dif)

    # Diferença entre todas as partidas
    aluno_maior_dif = maior_diferenca(vec_dif)
    print(f"\nAluno com a maior diferença: {aluno_maior_dif+1}")

if __name__ == "__main__":
    main()
