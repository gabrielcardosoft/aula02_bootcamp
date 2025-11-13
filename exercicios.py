# 04. Faça um programa que peça dois números interios e imprima a divisão inteira do primeiro pelo segundo.

first_value = int(input("Digite o primeiro número: "))
second_value = int(input("Digite o segundo número: "))
divisao = (first_value // second_value)
print(f"A divisão do primeiro valor pelo segundo valor é {divisao}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada

import math
raio_circulo = float(input("Digite o raio do círculo: "))
area_circulo = math.pi * raio_circulo ** 2
print(f"{area_circulo:.2f}")
