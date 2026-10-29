"""
import time
print('Exercício 046:')
print('═' * 15)

explosao = """ """
                  .
               .  :  .
             '  . : .  '
         .  *  .  :  .  *  .
      '  .  *  ·  :  ·  *  .  '
    .  ·  .  *  # # #  *  .  ·  .
 .  :  ·  *  # # # # # # #  *  ·  :  .
 : — — * — # # # ✳ # # # — * — — :
 ·  :  ·  *  # # # # # # #  *  ·  :  ·
    '  ·  .  *  # # #  *  .  ·  '
      .  '  *  ·  :  ·  *  '  .
         '  .  *  :  *  .  '
             .  ' : '  .
               '  :  '
                  .
""" """
tempo = int(input('Digite o tempo em segundos que vc quer esperar para ver a explosão: '))
for c in range(0,tempo):
    print("{:^}...".format(tempo-c))
    time.sleep(1)
print(explosao)


print("Exercício 047:\nEsses números a seguir são pares:")
print('═' * 15)

for c in range(1,50):
      if c%2 == 0:
            print('{}'.format(c))

print('Exercício 048:')
print('═' * 15)

soma = 0
for imp in range(1,500):
    if imp%3 == 0:
        soma = soma + imp
print('A somo dos valores impares de 1 a 500 é: {}'.format(soma))


print('Exercício 049:')
print('═' * 15)

tab = int(input('Digite um valor para ver sua tabuada: '))
for i in range(0, 11):
    print('{} x {} = {}'.format(tab, i, tab*i))

print('Exercício 051:')
print('═' * 15)

termo = float(input('Digite o valor do termo da PA: '))
razão = float(input('Digite o valor da razão: '))
print('Os primeiros números da sua PA são:')
for a in range(0, 10):
    print('{:.0f}'.format(termo),end='')
    termo = termo+razão
    if a<9:
        print(',',end='')
    else:
        print('.')

print('Exercício 052:')
print('═' * 15)

num= int(input('Digite um número e descubra se ele é primo: '))
primo = True
divisor = []
for n in range(1,num):
    if num%n == 0 and n != num and n != 1:
        primo = False
        divisor.append(n)
if primo == True:
    print('Esse número é primo.')
else:
    print('Esse número não é primo. Ele é divisivel por: {}'.format(divisor))
    """
print('Exercício 053:' )
print('═' * 15)

palavra = input('Digite uma palavra e veja se é um palindromo: ').lower()
tam = len(palavra)
met = int(tam/2)
palindromo =True
for i in range (0,met):
    seg_metade = palavra[met:]
    if seg_metade[i] != palavra[i]:
        
        palindromo =False
        break
    else:
       palindromo = True
if palindromo:
    print('Essa palavra é um palindromo.')
else:
    print('Essa palavra n é um palindromo.')
