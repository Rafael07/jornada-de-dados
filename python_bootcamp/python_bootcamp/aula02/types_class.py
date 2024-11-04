# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     celsius_temp = float(input("Enter a temperature in Celsius: "))
#     fahrenheit_temp = (celsius_temp * 9/5) + 32
#     print(f'This temperature is equivalent to {fahrenheit_temp} Fahrenheit.')

# except ValueError as ve:
#     print(f'The value entered is not valid, please try again.\n{ve}')

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# import re

# try:
#     palindrome = input("Type a word or sentence: ")
#     if isinstance(palindrome, str):
#         formated_output = re.sub(r'[^A-Za-z]', '', palindrome).lower()
#         if formated_output and formated_output == formated_output[::-1]:
#             print("It's a palindrome!!!")
#         else:
#             print("It's not a palindrome!!!")
# except ValueError as va:
#     print("Not a valid value entered, please try again.")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

n1 = float(input('Enter a number: '))
n2 = float(input('Enter a number: '))
op = input("Enter the desired operation based in the operators (+, -, *, /): ")

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:   
    print("This is not a valid option. ")


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar 
# o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.