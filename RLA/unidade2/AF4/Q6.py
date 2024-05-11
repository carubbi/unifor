# Questão 6 - Geração da sequência de Fibonacci (2 pontos)
# Gerar e imprimir os $n$ primeiros termos da sequência de Fibonacci, onde $n ≥ 1$. <br>
# Os primeiros termos são: $0, 1, 1, 2, 3, 5, 8, 13, \dots$. Cada termo, além dos dois primeiros, é derivado da soma dos seus dois antecessores mais próximos.

def gera_fibonacci(n: int) -> None:
    """Gera e imprime os primeiros n termos da série Fibonacci."""
    a: int = 0
    b: int = 1

    for i in range(1, n + 1):
        print(a, end=" ")

        termo_atual: int = a + b
        a, b = b, termo_atual

def main() -> None:
    n: int = 20
    gera_fibonacci(n)

if __name__ == "__main__":
    main()
