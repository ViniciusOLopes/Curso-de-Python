
def menu_principal():
    print('='*40)
    print('MENU PRINCIPAL'.center(40))
    print('='*40)
    print('\033[33m 1 -\033[0m \033[36mVer pessoas cadastradas\033[0m')
    print('\033[33m 2 -\033[0m \033[36mCadastrar nova Pessoa\033[0m')
    print('\033[33m 3 -\033[0m \033[36mSair do Sistema\033[0m')
    print('='*40)

def menu_cadastro():
    from utilidades.dados import models
    print('='*40)
    print('MENU CADASTRO'.center(40))
    print('='*40)
    while True:
        try:
            nome = str(input('Nome: '))
        except:
            print('\033[0;32m [ERRO] Nome não cadastrado.\033[0m')
            return
        else:
            while True:
                try:
                    idade = int(input('Idade: '))
                except:
                    print('\033[0;32m [ERRO] Idade não cadastrado.\033[0m')       
                else:
                    models.cadastrar_pessoa(nome,idade)
                    break
            break
               


def printar_pessoas_cadastradas():

    with open('banco.txt') as banco:
        dados = banco.readlines()
  
    print('=' * 40)
    print(f'|{"Nomes":<32}|{"Idade":>2}|')
    print('|'+'=' * 32 + '|' + '='*5 + '|')

    for pessoa in dados:
        dado = pessoa.strip().split(';')

        nome = dado[0].strip()
        idade = dado[1].strip()
        if int(idade) < 99:
            idade = f'.{idade}'
        elif int(idade) >999:
            idade = 'GDM'

        print(f'|{nome[:30].ljust(32,".")}|{idade:^5}|')

    print('=' * 40)
