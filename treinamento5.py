# Calculadora que soma o faturamento mensal durante o ano e forneçe a média final.

janeiro = float(input('Digite o valor do faturamento em Janeiro: '))
fevereiro = float(input('Digite o valor do faturamento em Fevereiro: '))
marco = float(input('Digite o valor do faturamento em Março: '))
abril = float(input('Digite o valor do faturamento em Abril: '))
maio = float(input('Digite o valor do faturamento em Maio: '))
junho = float(input('Digite o valor do faturamento em Junho: '))
julho = float(input('Digite o valor do faturamento em Julho: '))
agosto = float(input('Digite o valor do faturamento em Agosto: '))
setembro = float(input('Digite o valor do faturamento em Setembro: '))
outubro = float(input('Digite o valor do faturamento em Outubro: '))
novembro = float(input('Digite o valor do faturamento em Novembro: '))
dezembro = float(input('Digite o valor do faturamento em Dezembro: '))
soma = janeiro+fevereiro+marco+abril+maio+junho + \
    julho+agosto+setembro+outubro+novembro+dezembro
divisao = soma/12
print(f'A média de faturamento da empresa é: {divisao:.2f}')
