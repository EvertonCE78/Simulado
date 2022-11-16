"""#Questão 13
### Pedir 10 números, se o número for par, vai para uma lista, se for impar, vai para outra lista. Ao final, mostrar as duas listas, a soma dos pares, a soma dos impares e a soma das duas listas
"""

lista = []
contador = 1
pares = []
impares = []

while contador <= 10:
    numero = int(input(f"Digite o {contador}º número: "))
    contador +=1
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

somalistas = sum(pares)+sum(impares)

print("A lista dos números pares é:")
print(pares)
print("A lista dos números ímpares:")
print(impares)
print("A soma dos números pares é: ")
print(sum(pares))
print("A soma dos números ímpares: ")
print(sum(impares))
print("A soma dos números pares e ímpares: ")
print(somalistas)