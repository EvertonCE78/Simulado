"""# Questão 06
### 06. Um estacionamento cobra um valor mínimo de 10 reais, correspondente a 1h de uso. Cada hora adicional gera mais 5 reais de cobrança. Ex: um carro estacionado por 5 horas irá pagar 10 reais pela primeira hora + 5 reais pela segunda + 5 pela terceira + 5 pela quarta + 5 pela quinta, totalizando 30 reais.
### Faça um programa que pergunte para o usuário quanto tempo seu carro ficou estacionado e responde o valor em reais a ser pago.

###OBS: o estacionamento não considera minutos, tampouco horas fracionárias. Portanto, o seu programa não precisa se preocupar com isso. Se a pessoa ficou 5 horas e 2 minutos, ela passou de 5 horas, portanto ela deve digitar a hora inteira mais próxima: 6 horas.
"""
print("-"*50)
print("Bem-vindo(a) ao programa de cobrança de estacionamento!")
print("-"*50)

horas = int(input("Informe a quantidade de horas de permanência no estacionamento: "))
umahora = int(10)
maishoras = int(5)

if horas <= 1:
    print("Valor total a pagar é: R$ 10,00")
else:
    print(f'Valor total a pagar é: {umahora+maishoras*(horas - 1)}')

