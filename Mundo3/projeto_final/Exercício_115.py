from utilidades import dados
from utilidades import printar

print('='*70)
print('SEJA BEM VINDO AO PROGRAMA DE CADASTRO DE PESSOAS'.center(70))
print('='*70)
while True:
    escolha = dados.models.coletar_escolha()
    if escolha == 1:
        printar.models.printar_pessoas_cadastradas()
    elif escolha == 2:
        printar.models.menu_cadastro()
    elif escolha == 3:
        break


