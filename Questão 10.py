"""#Questão 10
### Peça 5 números e informe a soma e o maior número (OBS: sem utilizar listas)
"""
soma=0
maior=0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma = soma + numero
    if numero>maior:
        maior = numero

print(f'A soma dos números digitados é: {soma}')
print(f'O maior número digitado é: {maior}')

