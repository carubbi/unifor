# Questão 4 - Cálculo de uma série
# Dado um conjunto de $n$ termos da série, implemente e teste um algoritmo para calcular o valor de S, conforme definido abaixo:
# $$ S = \frac{1}{2} + \frac{3}{4} + \frac{5}{6} + \frac{7}{8} + \dots $$

def soma_serie(n: int) -> float:
    """
    Calcula a soma da série S mediante o número de termos informado.
    """
    S: float = 0

    for i in range(n):
        numerador: int = 2 * i + 1
        denominador: int = 2 * i + 2
        termo: float = numerador / denominador
        S += termo

    return S

def main() -> None:
    n: int = 4
    resultado: float = soma_serie(n)
    print(f"Soma da série S: {resultado:.2f}")

if __name__ == "__main__":
    main()
