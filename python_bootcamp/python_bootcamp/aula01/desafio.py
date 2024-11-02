"""Escreva um programa em Python que solicita ao usuário para digitar 
seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo 
nome e informando o valor do salário em comparação com o bônus recebido."""

user_name = input("Type our name: ")
user_salary = input("Type your salary: ")
bonus = input("Type the bonus that you earned: ")

kpi_bonus = 1000 + float(bonus)*int(user_salary)

print(f'Olá, {user_name}, o seu bônus foi de {kpi_bonus:.0f}')