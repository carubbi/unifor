# Questão 2
# Leia uma temperatura dada em Celsius (C) e imprima o equivalente em Fahrenheit (F). (Fórmula de conversão: F = (9/5) * C + 32)

def converter_celsius_fahrenheit():
    C = float(input("Digite a temperatura em Celsius: "))
    F = (9/5) * C + 32
    print(f"A temperatura em Fahrenheit é {F:.1f} graus")

if __name__ == "__main__":
    converter_celsius_fahrenheit()
