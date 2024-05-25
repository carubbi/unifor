"""
Questão 02 (6 pontos)

Você foi contratado para desenvolver um programa que ajude uma cafeteria a gerenciar as vendas de café de acordo com o orçamento dos clientes. Para isso, você deve criar funções que realizem as seguintes tarefas:

1. Solicitar e validar o orçamento do cliente.
2. Verificar o que o cliente pode comprar com seu orçamento e calcular o troco.
3. Armazenar os trocos de vários clientes.
4. Encontrar o maior troco entre os clientes.

Entradas obrigatórias:

Qual é o seu orçamento? 8
Qual é o seu orçamento? 3
Qual é o seu orçamento? 6
Qual é o seu orçamento? 10
Qual é o seu orçamento? 5

Saídas esperadas:

Qual é o seu orçamento? 8
Você pode comprar o café grande
Seu troco é 2. Volte sempre!

Qual é o seu orçamento? 3
Você pode comprar o café pequeno
Seu troco é 1. Volte sempre!

Qual é o seu orçamento? 6
Você pode comprar o café grande
Sem troco. Volte sempre!

Qual é o seu orçamento? 10
Você pode comprar o café grande
Seu troco é 4. Volte sempre!

Qual é o seu orçamento? 5
Você pode comprar o café médio

Trocos dos clientes: [2, 1, 0, 4, 0]

O maior troco é: 4
"""

def obter_orcamento_cliente() -> int:
    """
    Solicita ao cliente o orçamento e converte-o para um número inteiro.
    Lida com entrada inválida.
    """
    while True:
        try:
            return int(input('Qual é o seu orçamento? '))
        except ValueError as e:
            # print(e)
            print("Digite um valor válido!\n")
            continue

def verificar_orcamento(orcamento_cliente: int, pequeno: int, medio: int, grande: int) -> int:
    """
    Verifica o orçamento do cliente e imprime o que ele pode comprar.
    Retorna o troco se houver, caso contrário, retorna 0.
    """
    troco = 0
    msg = 'Sem troco. Volte sempre!\n'

    if orcamento_cliente > 0:
        if orcamento_cliente >= grande:
            print('Você pode comprar o café grande')
            if orcamento_cliente == grande:
                print(msg)
            else:
                troco = orcamento_cliente - grande
                print(f'Seu troco é {troco}. Volte sempre!\n')

        elif orcamento_cliente == medio:
            print('Você pode comprar o café médio')

        elif orcamento_cliente >= pequeno:
            print('Você pode comprar o café pequeno')
            if orcamento_cliente == pequeno:
                print(msg)
            else:
                troco = orcamento_cliente - pequeno
                print(f'Seu troco é {troco}. Volte sempre!\n')
    else:
        print('Não vendemos fiado!')

    return troco

def armazenar_trocos(nclientes: int, p: int, m: int, g: int) -> list:
    """
    Armazena os trocos de um número especificado de clientes.
    """
    trocos = [0] * nclientes
    for i in range(nclientes):
        orcamento = obter_orcamento_cliente()
        trocos[i] = verificar_orcamento(orcamento, p, m, g)

    return trocos

def maximo(vec: list) -> int:
    """
    Retorna o maior valor de uma lista.
    """
    maior: int = vec[0]
    n = len(vec)
    for i in range(1,n):
        if vec[i] > maior:
            maior = vec[i]

    return maior

def main() -> None:
    """
    Função principal para executar o programa.
    """
    PEQUENO = 2
    MEDIO = 5
    GRANDE = 6
    NUMERO_DE_CLIENTES = 5

    trocos = armazenar_trocos(NUMERO_DE_CLIENTES, PEQUENO, MEDIO, GRANDE)
    print('\nTrocos dos clientes:', trocos)
    maior_troco = maximo(trocos)
    print('\nO maior troco é:', maior_troco)

if __name__ == "__main__":
    main()
