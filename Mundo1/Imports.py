import math
import random
"""
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('Raiz de {} é {}'.format(num, math.floor(raiz)))
"""
print('Exercício 019:')
alunos = [0]*4

for i in range (4):
    aluno_nome = input('Digite o nome do {} aluno: '.format(i+1))
    alunos[i] = aluno_nome

aluno_escolhido = random.randint(0,3)

print('O aluno escolhido foi: {}'.format(alunos[aluno_escolhido]) )

"""
print('Exercício 017:')
cat_op = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(pow(cat_adj,2)+pow(cat_op,2))
print('A hipotenusa é: {}'.format(hipotenusa))

"""

print('Exercício 020: \nLista de sorteio do trabalho:')
lista_sorteio = list(range(0,4))
primeiro_sorteio = random.choice(lista_sorteio)
lista_sorteio.remove(primeiro_sorteio)

segundo_sorteio = random.choice(lista_sorteio)
lista_sorteio.remove(segundo_sorteio)

terceiro_sorteio = random.choice(lista_sorteio)
lista_sorteio.remove(terceiro_sorteio)

quarto_sorteio = random.choice(lista_sorteio)

print("A lista de sorteados é: \n1°{} \n2°{} \n3°{} \n4°{}\n".format(alunos[primeiro_sorteio],alunos[segundo_sorteio],alunos[terceiro_sorteio],alunos[quarto_sorteio]))


lista_sorteio = list(range(0,4))
for i in range (4):
    primeiro_sorteio = random.choice(lista_sorteio)
    lista_sorteio.remove(primeiro_sorteio)
    print("A lista de sorteados usando for é: \n{}° {}\n".format((i+1),alunos[primeiro_sorteio]))

print('Exercício 021: ')
