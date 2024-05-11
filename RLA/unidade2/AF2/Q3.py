# Questão 3
# Receba dois números reais e um operador e efetue a operação correspondente com os valores recebidos (operandos).<br>
# O algoritmo deve retornar o resultado da operação selecionada simulando todas as operações de uma calculadora simples.

def calculadora_simples():
    print("Operações válidas: 1 (soma), 2 (subtração), 3 (multiplicação) e 4 (divisão)")
    op = int(input("Digite uma operação: "))
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if op == 1:
        res = num1 + num2
        print(f"{num1} + {num2} = {res}")
    elif op == 2:
        res = num1 - num2
        print(f"{num1} - {num2} = {res}")
    elif op == 3:
        res = num1 * num2
        print(f"{num1} * {num2} = {res}")
    elif op == 4:
        if num2 != 0:
            res = num1 / num2
            print(f"{num1} / {num2} = {res}")
        else:
            print("Impossível dividir!")
    else:
        print("Operação inválida!")

if __name__ == "__main__":
    calculadora_simples()
