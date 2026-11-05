import moeda_108


num = float(input('Digite um preço: R$ '))
dup = moeda_108.dobro(num)
print(f'O dobro de {moeda_108.moeda(num)} é {moeda_108.moeda(dup)}')
print(f'A metade de {moeda_108.moeda(num)} é {moeda_108.moeda((moeda_108.metade(num)))}')
print(f'Ao diminuir 20% de {moeda_108.moeda(num)} temos {moeda_108.moeda(moeda_108.diminuir(num,20))}')
print(f'Ao aumentar 20% de {moeda_108.moeda(num)} temos {moeda_108.moeda(moeda_108.aumentar(num,20))}')