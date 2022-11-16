"""#Questão 14
### Programa para cálculo de IMC e ao final informar em qual categoria o usuário se encontra.
Obs: Pesquisar as categorias do IMC
"""
print("-"*50)
print("Bem-vindo(a) ao programa de cálculo do IMC!")
print("-"*50)

peso= float(input("Informe o seu peso em quilos: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso/(altura*altura)
print(imc)

if imc > 40:
    print("Obesidade III")
elif imc >= 35 and imc<=39.9:
    print("Obesidade II")
elif imc >= 30 and imc<=34.9:
    print("Obesidade I")
elif imc >= 25 and imc<=29.9:
    print("Acima do peso")
elif imc >= 18.5 and imc<=24.9:
    print("Peso normal")
else:
    print("Abaixo do peso")