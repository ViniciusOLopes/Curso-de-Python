import moeda

num = int(input('Digite um valor: '))
dup = moeda.dobro(num)
print(f'O dobro de {num} = {dup}')
print(f'A metade de {num} = {moeda.metade(num)}')
print(f'Ao diminuir 20% de {num} temos {moeda.diminuir(num,20)}')
print(f'Ao aumentar 20% de {num} temos {moeda.aumentar(num,20)}')
