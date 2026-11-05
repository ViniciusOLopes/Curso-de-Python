def leiaDinheiro(texto = 'Digite valor: '):
    continuar = True
    while continuar:
        num = input(texto)
        if num.isnumeric():
            continuar = False
            return float(num)
        else:
            print(f'\033[31m [ERRO] {num}, não é um valor válido!!\033[0m')
            continuar =True