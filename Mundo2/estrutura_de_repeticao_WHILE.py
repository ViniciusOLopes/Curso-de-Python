from dataclasses import dataclass
import os
'''
print('Exercício 58:')
print('═' * 15)

sexo = input('Escreva seu sexo/ genero:\nEscreva M para masculino, F para feminino e O para outro: ')
while sexo != 'M' and sexo != 'F' and sexo != 'O':
    print('Opção n identificada: ')
    sexo = input('Escreva seu sexo/ genero:\nEscreva M para masculino, F para feminino e O para outro: ')
if sexo == 'O':
    print('Você selecionou O, outro.')
elif sexo == 'F':
    print('Você selecionou F, Feminino.')
else:
    print('Você escolheu M, Masculino.')

print('Exercício 59:')
print('═' * 15)

opçao:int = 0
while opçao != 5:
    num1 = float(input('Escolha o primeiro número: '))
    num2 = float(input('Escolha o segundo número: '))
    trocar = 0
    while trocar != 2:
        opçao = int(input('Escolha uma opção a seguir: \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\n_'))
        match opçao:
            case 1:
                print('O valor da soma {} + {} = {}'.format(num1, num2, num1 + num2))
            case 2:
                print('O valor da multiplicação {} x {} = {}'.format(num1, num2, num1 * num2))

            case 3:
                if num1>num2:
                    print('{} é amior que {}'.format(num1, num2))
                if num2>num1:
                    print('{} é amior que {}'.format(num2, num1))
            case 4:
                break
            case 5:
                break
            case _:
                print('Opção inesistente.')
        trocar = int(input('Gostaria de manter os números? \nManter [1] \nTrocar [2]\n'))
        if trocar != 1 or trocar != 2:
            trocar = 2
            print('Opção invalida. Reescreva os números.')
        if opçao == 5: break

print('Fim do programa, obrigado por participar.')

print('Exercício 060:')
print('═' * 15)

num = int(input('Digite um número para descobrir seu fatorial: '))
print('{}! = '.format(num), end='')
fat = 1
while num >1:
    print('{} x '.format(num), end='')

    fat = fat*num
    num = num-1
print('1 = {}'.format(fat))

print('Exercício 065:')
print('═' * 15)

num = 'A'
max = -999999999
min = 9999999999
soma:int = 0
while num != 'n':
    rep = int(input('Quantos números quer digitar?_ '))
    for i in range(rep):
        n = int(input('Digite o número: '))
        soma = soma + n
        if n < min:
            min = n
        if n > max:
            max = n
    num = input('Quer continuar digitando númeoros?\n S/N_ ').lower()
print('A soma dos digitos é: {}\nO maior digitado: {}\nO menor: {}'.format(soma, max, min))

print('Exercio 069')
print('═' * 15)


@dataclass
class Pessoa:
    nome: str
    idade: int
    sexo: str

print('Cadastre seus dados: ')
cadastro  = []
a: str = 'a'
i: int = 0
while True:
    nome = input('Digite seu nome:')
    sexo = input('Digite seu sexo M (Masculino), F (Feminino), O(Outros): ').upper()
    while sexo != 'M' and sexo != 'F' and sexo != 'O':
        print('O valor digitado de sexo n é permitido !!!')
        sexo = input('Digite seu sexo M (Masculino), F (Feminino), O(Outros): ').upper()
    idade = int(input('Digite sua idade: '))
    cadastro.append(Pessoa(nome, idade, sexo))
    
    cont = input('Cadastro realisado com sucesso, Deseja continuar cadastrando novas pessoas? S/N: ').upper()
    if cont == 'N':
        break
    elif cont == 'S':
        pass
    else:
        while cont != 'S' and cont != 'N':
            print('Resposta n corresponde a nenhuma das opções: ')
            cont = input('Cadastro realisado com sucesso, Deseja continuar cadastrando novas pessoas? S/N: ').upper()
print('Imprimindo as Pessoas cadastradas: ')
maior18 = 0
menor20 = 0
homem = 0
for i in range (len(cadastro)):
    print('Pessoa {}\nNome: {}\nIdade: {}\nSexo: {}\n'.format(i+1, cadastro[i].nome, cadastro[i].idade, cadastro[i].sexo))
    if cadastro[i].idade >= 18:
        maior18 = maior18 +1
    if cadastro[i].sexo== 'F' and cadastro[i].idade < 20:
        menor20 = menor20 + 1
    if cadastro[i].sexo == 'M':
        homem = homem +1
print('quantos homens foram cadastrados: {}'.format(homem))
print('Quantas pessoas tem mais de 18 anos: {}'.format(maior18))
print('mulher menor que 20 anos: {}'.format(menor20))

'''
resp = str(input('Digite uma letra: ')).strip().upper()[0] 
print (resp)
for c in range(0, 10, 3):
    print (c)
print('Exercícios 071:')

saque = int(input('Digite o valor que deseja sacar: '))
n50 = int(saque/50)
n20 = int((saque%50)/20)
n10 = int(((saque%50)%20)/10)
n1 = int((((saque%50)%20)%10))

print('{} notas de 50, \n{} notas de 20, \n{} notas de 10, \n{} moedas de 1'.format(n50, n20, n10, n1))

