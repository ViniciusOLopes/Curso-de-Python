"""
frase = '  Curso em Vídeo Python          '
print('\n{}'.format(frase[::]))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase.find('Curso'))
dividido = frase.split()
print(dividido[::][::])

print('Exercício 022:')

nome = input('Digite seu nome completo: ')
print('\nNome completamente em maiusculo: {}\n'.format(nome.upper()))
print('Nome completo tudo minúsculo: {}\n'.format(nome.lower()))
print('O número de letras do seu nome = {}\n'.format(nome.strip()))
dividido = nome.split()

print('Seu primeiro nome é: {}, e tem {}, letras\n'.format(dividido[0], len(dividido[0])))


print('Exercício 023:')
numero = input('Escreva um número de 0 a 9999: ')
print('\nForma matemática:\n')
num = int(numero)
num_unidade = ((num%1000)%100)%10
num_dezena = ((num%1000)%100 -num_unidade)
num_centena = (num%1000 - num_dezena -num_unidade)
num_milhar = (num - num_centena - num_dezena - num_unidade)

print('milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}\n'.format(num_milhar/1000, num_centena/100, num_dezena/10, num_unidade))
print('Forma de string:\n')
print('milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}\n'.format(numero[0],numero[1],numero[2],numero[3]))

"""
print('Exercício 027:\n')
nome_completo = input('Digite seu nome completo: ')
nomes = nome_completo.split()
p_nome = nomes[0]
tam_nomes = len(nomes)
u_nome = nomes[tam_nomes-1]

print('Primeiro nome: {}\nUltimo nome: {}'.format(p_nome,u_nome))