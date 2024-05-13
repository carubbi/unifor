"""
Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de objetos. O vendedor recebe, mensalmente, salário de R$545,00, 
acrescido de 5% do valor total de suas vendas. O valor unitário dos objetos deve ser informado e armazenado em um vetor; a quantidade vendida de 
cada peça deve ficar em outro vetor, mas na mesma posição. Crie um programa que receba os preços e as quantidades vendidas, armazenando-os em seus 
respectivos vetores (ambos com tamanho dez). 

Depois determine e mostre:
A. um relatório contendo: a quantidade vendida, valor unitário e valor total de cada objeto. Ao final, deverão ser mostrados o valor geral das vendas 
e o valor da comissão que será paga ao vendedor; e
B. o valor do objeto mais vendido e sua posição no vetor (não se preocupe com empates).

1. Implemente a subfunção `produto_quantidade` para preencher os vetores de preços e quantidades dos produtos (1 ponto);
2. Implemente a subfunção `total_vendas` para calcular o total geral vendido e exibir as quantidade, preço e total de cada produto (1 ponto);
3. Implemente a subfunção `comissao` para calcular a comissão de vendas (1 ponto);
4. Implemente a subfunção `maior_produto` para definir o preço do produto com a maior quantidade vendida (2 ponto);
5. Implemente a função principal `main` a fim de chamar as subfunções e exibir os resultados exigidos de acordo com as entradas obrigatórias (1 ponto).
"""

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
