"""#Questão 04
###Faça um programa que solicite a nota das 4 provas de um aluno e responde a sua média.
"""
soma=0
contador=0

while contador <4:
    nota = float(input(f' Entre com o valor da {contador +1}ª nota: '))
    soma = soma + nota
    contador +=1

media = soma/contador

print(f' A média das provas é: {media}')



