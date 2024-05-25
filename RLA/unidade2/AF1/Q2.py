# Questão 2
# Implemente em Python, um algoritmo para calcular o novo salário de um funcionário. 
# Sabe-se que os funcionários que recebem atualmente salário de até R$ 500 terão aumento de 20%; 
# os demais terão aumento de 10%.

def reajuste_salario():
    sal_atual = float(input("Digite seu salário atual: "))

    if sal_atual <= 500:
        sal_reaj = sal_atual * 1.2
    else:
        sal_reaj = sal_atual * 1.1

    print(f"O novo salário é R$ {sal_reaj:.2f}")

if __name__ == "__main__":
    reajuste_salario()
