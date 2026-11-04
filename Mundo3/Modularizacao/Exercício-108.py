import moeda

def monetario(num:int):
    return f'R${num:.2f}'


num = int(input('Digite um valor: '))
dup = moeda.dobro(num)
print(f'O dobro de {monetario(num)} é {monetario(dup)}')
print(f'A metade de {monetario(num)} é {monetario(moeda.metade(num))}')
print(f'Ao diminuir 20% de {monetario(num)} temos {monetario(moeda.diminuir(num,20))}')
print(f'Ao aumentar 20% de {monetario(num)} temos {monetario(moeda.aumentar(num,20))}')