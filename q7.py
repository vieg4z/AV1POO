'''Questão 7 (1 ponto): Faça um programa que receba o valor de uma dívida e mostre uma tabela com
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Tabela de juros sobre a quantidade de parcelas
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25

Exemplo de saída do programa:

|Dívida | Juros |Quantidade de Parcelas | Valor da Parcela|
|R$ 1.000,00 | 0 | 1 | R$ 1.000,00 |
|R$ 1.100,00 | 100 | 3 | R$ 366,00 |
|R$ 1.150,00 | 150 | 6 | R$ 191,67 |
'''
# Solicitar o valor da dívida ao usuário
divida = float(input("Digite o valor da dívida: R$ "))

# Cabeçalho da tabela
print("| Dívida       | Juros | Qtd Parcelas | Valor da Parcela |")
print("|--------------|-------|--------------|------------------|")

# Tabela de parcelas e taxas
parcelas = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

for quantidade, taxa in parcelas:
    juros = divida * (taxa / 100)
    total = divida + juros
    parcela = total / quantidade
    print(f"| R$ {total:.2f} | R$ {juros:.2f} | {quantidade:12} | R$ {parcela:.2f} |")
