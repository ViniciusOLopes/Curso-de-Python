from moeda_109 import moeda
from moeda_109 import dobro
from moeda_109 import metade
from moeda_109 import diminuir
from moeda_109 import aumentar


num = float(input('Digite um preço: R$ '))
print(f'O dobro de {moeda(num)} é {dobro(num,True)}')
print(f'A metade de {moeda(num)} é {metade(num,True)}')
print(f'Ao diminuir 20% de {moeda(num)} temos {diminuir(num,20,True)}')
print(f'Ao aumentar 20% de {moeda(num)} temos {aumentar(num,20, True)}')