# Questão 2 - Contagem
# Dado um conjunto $n$ de notas de alunos em um exame, implemente e teste um algoritmo para fazer uma contagem $cont$ do número de alunos que foram aprovados no exame.
# Será considerado aprovado o aluno que tirar $nota$ 50 ou maior (no intervalo de 0 a 100).

def conta_aprovacoes(n: int) -> None:
    """
    Conta o número de alunos aprovados.
    """
    cont: int = 0
    i: int = 1

    while i <= n:
        nota: float = float(input(f"Digite a nota do aluno {i}: "))
        if nota >= 50 and nota <= 100:
            cont += 1
        i += 1

    print("O número de alunos aprovados é:", cont)

def main() -> None:
    """Função principal que solicita o número de notas dos alunos."""
    n: int = int(input("Digite a quantidade de notas dos alunos: "))
    conta_aprovacoes(n)

if __name__ == "__main__":
    main()
