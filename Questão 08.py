"""# Questão 08
### Crie um algoritmo que indique se um número é positivo ou negativo
"""
print("-"*50)
print("Bem-vindo(a) ao programa positivo ou negativo!")
print("-"*50)

numero = float(input("Digite um número: "))

if numero >0:
    print("O número é positivo")
elif numero <0:
    print("O número é negativo")
else:
    print("O número é neutro")