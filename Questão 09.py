"""#Questão 09
### Crie um algoritmo que indique se um número é par ou impar
"""
print("-"*50)
print("Bem-vindo(a) ao programa par ou ímpar!")
print("-"*50)

numero= int(input("Digite um número e veja se ele é par ou ímpar: "))

if numero % 2 == 0:
    print("É um número par")
else:
    print("É um número ímpar")