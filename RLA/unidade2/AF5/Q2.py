def preenche_vetor(n: int) -> list[float]:
    """
    Preenche os vetores com os preços e quantidades dos produtos e retorna os
    respectivos vetores.
    """
    vec: list[float] = [0.] * n

    for i in range(n): # 0,1,2,..., n-1
        vec[i] = float(input(f"Digite o valor {i + 1}: "))

    return vec

def prod_qtd(n: int) -> list[float] and list[int]:
    """
    Preenche os vetores com os preços e quantidades dos produtos e retorna os
    respectivos vetores.
    """
    preco: list[int] = [0] * n
    qtd: list[int] = [0] * n

    for i in range(n):
        preco[i] = float(input(f"Digite o preço do produto {i + 1}: "))
        qtd[i] = int(input(f"Digite a quantidade vendida do produto {i + 1}: "))
        print()

    return preco, qtd

def total_vendas(preco: list[float], qtd: list[int]) -> float:
    """
    Retorna as vendas totais e exibe as vendas de cada produto.
    """
    n: int = len(preco)
    tot_geral: int = 0
    for i in range(n):
        tot_vend: float = qtd[i] * preco[i]
        print(f"R$: {preco[i]} Qtd: {qtd[i]} Total: {tot_vend}")
        tot_geral += tot_vend # tot_geral = tot_geral + tot_vend

    return tot_geral

def comissao(tot_geral: float, taxa: int = 5) -> float:
    """
    Calcula a comissão.
    """
    return tot_geral * taxa / 100


def maior_prod(preco: list[float], qtd: list[int]) -> float and int:
    """
    Retorna o preço do produto com a maior quantidade vendida.
    """
    maior: int = qtd[0]
    imaior: int = 0
    n: int = len(qtd)
    for i in range(1, n):
        if qtd[i] > maior:
            maior = qtd[i]
            imaior = i

    return preco[imaior], maior

def main() -> None:
    p, q = prod_qtd(10)
    t = total_vendas(p, q)
    c = comissao(t)
    print(f"\nTotal Geral: R$ {t:.2f} Comissão: R$ {c:.2f}")
    mp, mq = maior_prod(p,q)
    print(f"Objeto mais vendido: R$ {mp:.2f} Qtd: {mq}")

if __name__ == "__main__":
    main()
