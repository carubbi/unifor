# Questão 2 - Contagem
# Dado um conjunto $n$ de notas de alunos em um exame, implemente e teste um algoritmo para fazer uma contagem $cont$ do número de alunos que foram aprovados no exame.
# Será considerado aprovado o aluno que tirar $nota$ 50 ou maior (no intervalo de 0 a 100).

def conta_aprovacoes(n: int) -> int:
    """
    Conta o número de alunos aprovados com notas entre 50 e 100.
    """
    cont: int = 0

    for i in range(1, n + 1):
        nota = float(input(f"Digite a nota do aluno {i}: "))
        if nota >= 50 and nota <= 100:
            cont += 1

    print(f"O número de alunos aprovados: {cont}")

def main():
    n: int = 3
    conta_aprovacoes(n)

if __name__ == "__main__":
    main()
