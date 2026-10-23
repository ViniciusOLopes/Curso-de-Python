"""
print('Exercício 029:')
velocidade = float(input('\nEscreva a velocidade do seu carro: '))

if velocidade >80:
    velocidade_acima = velocidade -80
    multa = velocidade_acima*7
    print('Você ultrapassou a velocidade máxima de 80 Km/h em {}Km/h.' \
    '\nO valor da multa é R$7,00 para cada km acima do limite permitido,'\
    'você deve pagar: R${:.2f}'.format(velocidade_acima, multa))
else:
    print('Parabens vc n ultrapassou o limite de velocidade.')


print('Exercício 030:')
num = int(input('Digite algum numero: '))
print('Par' if num%2 <=0 else 'Impar')

print('Exercício 034:')
salario = float(input('Digite o valor do seu salário: '))
print('Seu novo salário é: R${:.2f}. Você recebeu 10 porcento de aumento'.format(salario*1.1) if salario >=1250 else 'Seu novo salário é: R${:.2f}. Você recebeu 15 porcento de aumento'.format(salario*1.15))

print('Exercício 035:')
r1 = float(input('Digite o valor de r1: '))
r2 = float(input('Digite o valor de r2: '))
r3 = float(input('Digite o valor de r3: '))

print('Essas retas n formão um triângulo' if r1+r2<r3 or r1+r3<r2 or r2 + r3<r1 else 'Essas retas formam um triângulo')
"""
