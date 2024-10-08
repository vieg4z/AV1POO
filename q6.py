'''Questão 6 (1 ponto): Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
que esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00. Faça um programa
que determine o salário desse funcionário em 2025, sabendo que:
* Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
* A partir de 1997 (inclusive),
'''

salario = 1000.00
salario *= 1.015  # Aumento de 1,5% em 1996

for _ in range(29):  # Aumentos de 2% de 1997 a 2025
    salario *= 1.02

print(f"Salário em 2025: R$ {salario:.2f}")

