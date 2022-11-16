"""#Questão 05
### Crie um algoritmo que informe o tipo de um valor informado pelo usuário
"""
print("-"*50)
print("Bem-vindo(a) ao programa de tipos de entrada!")
print("-"*50)

print("Escolha o tipo de número que você irá digitar: ")
entrada = int(input( "[1] - Inteiro"
                 "\n[2] - Float"
                 "\n[3] - String"
                 "\n[4] - Boleano (0 ou 1)\n"))

if entrada == 1:
  valor = int(input("Digite o número inteiro: "))
  tipo = type(valor)
  print(f'Você digitou o número {valor} que é do tipo {tipo}')
elif entrada == 2:
    valor = float(input("Digite o número float: "))
    tipo = type(valor)
    print(f'Você digitou o número {valor} que é do tipo {tipo}')
elif entrada == 3:
    valor = str(input("Digite o texto: "))
    tipo = type(valor)
    print(f'Você digitou o texto {valor} que é do tipo {tipo}')
elif entrada == 4:
    valor = bool(input("Digite 0 ou 1: "))
    tipo = type(valor)
    print(f'Você digitou o texto {valor} que é do tipo {tipo}')
else:
    print("Opção inválida!!!")