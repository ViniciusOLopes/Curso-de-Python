p = input ('Digite alguma coisa: ')

print('O tipo primitivo desse valor é {}'.format(type(p)))
print('Só tem espaço? {}'.format( p.isspace()))
print('É um número?  {}'.format( p.isnumeric()))
print('É alfabético? {}'.format( p.isalpha()))
print('É alfanumérico? {}'.format( p.isalnum()))
print('Está em maiusculas? {}'.format(p.isupper()))
print('Está em minúsculas {}'.format(p.islower()))


