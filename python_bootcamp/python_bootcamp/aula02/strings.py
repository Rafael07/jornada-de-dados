# Strings (str)
# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# Escreva um programa que concatene duas strings fornecidas pelo usuário.

print("\nQuestão 1")
n1 = (input("Enter a name: "))
print(n1.upper())

print("\nQuestão 2")
n1 = (input("Enter you full name: "))
print(n1.lower())

print("\nQuestão 3")
n1 = (input("Enter any sentence: "))
print(n1.strip())

print("\nQuestão 4")
n1 = (input("Enter any date in the format dd/mm/yyyy: "))
print(n1.split("/"))

print("\nQuestão 5")
n1 = (input("Enter anything: "))
n2 = (input("Enter anything: "))

print(n1+n2)