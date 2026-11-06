from utilidades.printar.models import menu_principal 

def coletar_escolha():
    while True:
        menu_principal()
        try:
            escolha = int(input('\033[33mSua Opção: \033[0m'))
        except ValueError:
            print('\033[0;31m[ERROR] Escolha uma das opções disponiveis.\033[0m')
        else:
            if escolha > 3:
                print('\033[0;31m[ERROR] Escolha uma das opções disponiveis.\033[0m')
                continue
            else: return escolha


def cadastrar_pessoa(nome:str, idade:int):
    try:
        banco = open('banco.txt','a')
    except:
            print('\033[0;32m [ERRO] Ao tentar acessar o arquivo de cadastos ouve um pronblema.')
    else:
            banco.write(f'{nome};{idade}\n')
            banco.close()

