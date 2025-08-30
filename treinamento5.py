# Calculadora que soma o faturamento mensal durante o ano e forneçe a média final.

print('Soma de faturamento mensal e média de faturamento')

jan = float(input('Digite o valor do faturamento de Janeiro: '))
fev = float(input('Digite o valor do faturamento de Fevereiro: '))
mar = float(input('Digite o valor do faturamento de Março: '))
abr = float(input('Digite o valor do faturamento de Abril: '))
mai = float(input('Digite o valor do faturamento de Maio: '))
jun = float(input('Digite o valor do faturamento de Junho: '))
jul = float(input('Digite o valor do faturamento de Julho: '))
ago = float(input('Digite o valor do faturamento de Agosto: '))
set = float(input('Digite o valor do faturamento de Setembro: '))
out = float(input('Digite o valor do faturamento de Outubro: '))
nov = float(input('Digite o valor do faturamento de Novembro: '))
dez = float(input('Digite o valor do faturamento de Dezembro: '))
soma = jan+fev+mar+abr+mai+jun+jul+ago+set+out+nov+dez
divisao = soma/12
print(f" A soma anual de faturamento é R$: {soma:,.2f}')
print(f'A média mensal de faturamento é R$: {divisao:,.2f}')


