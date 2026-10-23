print('Exercício 006:')
num = int(input('Digite um número e vc descobrirá seu antesseçor e sucessor: '))
ant = num-1
suc = num+1
print('O sucessor do número digitado é: {}! \nSeu antecessor é: {}!'.format(suc, ant))

print('Exercício 007:')
num_2 = float(input('Digite algum número e descubra seu dobro, triplo e raiz quadrada: '))
raiz = num_2**(1/2)
dobro = num_2**2
triplo = num_2**3
print('Dobro: {} \nTriplo: {} \nRaiz: {:.4}'.format(dobro, triplo, raiz))

print('Exercício 015:')
num_3 = float(input('Digite quantos quilómetros que vc andou no carro: '))
num_4 = int(input('Digite quantos dia ficou com o carro: '))
km = num_3*0.15
dias = num_4*60
print('O valor por dias com o carro: {} \nO valor por km roados: {} \nO valor a pagar é: {}'.format(dias, km, (dias + km)))