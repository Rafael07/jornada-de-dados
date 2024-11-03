# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

print("\nQuestão 1")
s1 = input("True or False: ")
s2 = input("True or False: ")

bool1 = s1.strip() == "True"
bool2 = s2.strip() == "True"

print(s1 and s2)