"""
print('Exercício 36:')
print('═' * 15)

salario = float(input('Digite o seu salario:'))
preco_casa = float(input('Digite o valor da casa: '))
tempo = int(input('Digite o valor em anos que vc quer pagar a casa:'))

parcela = preco_casa/ (tempo*12)

if salario*0.3< parcela:
    print('A casa esta fora do seu orçamento.')
else:
    print('A casa esta no seu orçamento.')
print('As parcelas são de R${:.2f}'.format(parcela))
"""
