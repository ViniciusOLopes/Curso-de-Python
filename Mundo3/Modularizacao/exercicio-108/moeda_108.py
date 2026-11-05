def aumentar(num=0,p=0):
    return num*(1+(p/100))


def diminuir(num=0,p=0):
    return num*(100-p)/100


def dobro(num=0):
    return num * 2


def metade(num=0):
    return num / 2

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')