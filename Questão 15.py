"""#Questão 15
### Solicite a idade de 5 pessoas e ao final conte quantas pessoas são maiores de idade, a soma de todas as idades, a média das idades, o valor máximo, o valor mínimo, ordene de forma crescente e decrescente.
"""

idades = []
contador = 1
testeidade = 0

while contador <= 5:
    numero = int(input(f"Digite o {contador}ª idade: "))
    contador +=1
    idades.append(numero)
    if numero >= 18:
        testeidade +=1

print(f'A soma das idades é: {sum(idades)}')
print(f'Temos {testeidade} pessoas maiores de idade')
print(f'A ')