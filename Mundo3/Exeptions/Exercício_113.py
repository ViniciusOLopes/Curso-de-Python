print('Exercício 104: ')
print('═' * 15)

import sys

def leiaInt(text='Digite um valor inteiro: ', text2 = 'Digite um valor real: '):
    lib = False
    while lib != True:
        try:
            num = int(input(text+':'))
        
        except ValueError:
            print(f'\033[0;31mERRO! {text}.\033[0m')

        except KeyboardInterrupt:
            print('\033[0;31m\n[ERRO] O usuário decidiu n digitar atribuindo assim o valor 0 como padrão.\033[0m')
            lib = True
            return 0

        else:
            lib = True
            return num
 
def leiaFloat(text2):
    lib = False
    while lib != True:
            try:
                num2 = float(input(text2+':'))
            
            except (ValueError):
                print(f'\033[0;31m[ERRO!] {text2}.\033[0m')

            except KeyboardInterrupt:
                print('\033[0;31m\n[ERRO] O usuário decidiu n digitar atribuindo assim o valor 0 como padrão.\033[0m')
                lib = True
                return 0
    
            else:
                lib = True
                return num2
                 

num =leiaInt('Digite um valor INTEIRO ')
num2 = leiaFloat('Digite um valor REAL ')
print(f'O número {num} é inteiro e o numero {num2:.1f} é real')

