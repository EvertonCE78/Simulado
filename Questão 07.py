"""# Questão 07
### 07. Faça um programa que pergunta a temperatura em graus Celsius e responde a temperatura correspondente em graus Fahrenheit.

### 07.1 Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius.
"""

print("-"*50)
print("Bem-vindo(a) ao programa de conversão de escala de temperatura!")
print("-"*50)

print("Escolha a conversão de temperatura: ")
escala = int(input( "[1] - Celsius para Fahrenheit"
                 "\n[2] - Fahrenheit para Celsius\n"))

if escala == 1:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius *9/5)+32
    print(f'O valor de {celsius} graus Celsius em Fahrenheit é: {fahrenheit}')
elif escala == 2:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = (fahrenheit-32)/1.8
    print(f'O valor de {fahrenheit} graus Fahrenheit em Celsius é: {celsius}')
else:
    print("Opção inválida!!!")