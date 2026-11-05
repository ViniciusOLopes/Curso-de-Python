def aumentar(num=0,p=0,formatado=False, monetario='R$'):
    """Aumenta um valor em um determinado percentual.

    Args:
        num (int, float): O valor numérico inicial.
        p (int, float): A porcentagem do aumento (ex: 10 para 10%).
        formatado (bool): Se True, retorna o valor formatado como moeda.
        monetario (string): Sera usado na formatação da moeda.

    Returns:
        float, str: O valor aumentado. Retorna str se formatado=True, senão float.
    """
    
    if formatado:
        num = num*(1+(p/100))
        return moeda(num, monetario)
    return num*(1+(p/100))


def diminuir(num=0,p=0,formatado=False, monetario='R$'):
    """Diminui um valor em um determinado percentual.

    Args:
        num (int, float): O valor numérico inicial.
        p (int, float): A porcentagem do desconto (ex: 10 para 10%).
        formatado (bool): Se True, retorna o valor formatado como moeda.
        monetario (string): Sera usado na formatação da moeda.

    Returns:
        float, str: O valor reduzido. Retorna str se formatado=True, senão float.
    """
    
    if formatado:
        num = num*(100-p)/100
        return moeda(num, monetario)
    return num*(100-p)/100


def dobro(num=0,formatado=False, monetario='R$'):
    """Calcula o dobro de um número.

    Args:
        num (int, float): O número a ser dobrado.
        formatado (bool): Se True, retorna o valor formatado como moeda.
        monetario (string): Sera usado na formatação da moeda.

    Returns:
        int, float, str: O dobro do número. Retorna str se formatado=True.
    """
    
    if formatado:
        num = num*2
        return moeda(num, monetario)
    return num * 2


def metade(num=0,formatado=False, monetario='R$'):
    """Calcula a metade de um número.

    Args:
        num (int, float): O número a ser dividido por dois.
        formatado (bool): Se True, retorna o valor formatado como moeda.
        monetario (string): Sera usado na formatação da moeda.

    Returns:
        float, str: A metade do número. Retorna str se formatado=True.
    """
    
    if formatado:
        num = num/2
        return moeda(num, monetario)
    return num / 2

def moeda(preco = 0, moeda = 'R$'):
    """Formata um número real no padrão monetário brasileiro.

    Args:
        preco (int, float): O valor a ser formatado.
        moeda (str): O símbolo da moeda a ser utilizado (padrão: 'R$').

    Returns:
        str: O valor formatado com o símbolo da moeda e duas casas decimais.
    """

    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(num=0,diminuicao=0,aumento=0, formatar=False, monetario='R$'):
    """Resume todos as possiveis funções de uma vez, já deixando formatado

    Args:
        num (int, float): O valor a ser formatado.
        diminuicao (int, float): A porcentagem do desconto (ex: 10 para 10%).
        aumento (int, float): A porcentagem do acrescimo (ex: 10 para 10%).)
        formatar (bool): Se True, retorna o valor formatado como moeda.
        monetario (str): O símbolo da moeda a ser utilizado (padrão: 'R$').

    Returns:
        string: Uma pequena tabela com todos os valores ajustados
    """

    print('=-'*20)
    if formatar:
        print(f'Preço analisado..........{moeda(num, monetario)}')
        print(f'Dobro do preço...........{dobro(num,True, monetario)}')
        print(f'Metade do preço..........{metade(num,True, monetario)}')
        print(f'{diminuicao}% de redução...........{diminuir(num,diminuicao,True, monetario)}')
        print(f'{aumento}% de aumento...........{aumentar(num,aumento, True, monetario)}')
    else:
        print(f'Preço analisado..........{num}')
        print(f'Dobro do preço...........{dobro(num)}')
        print(f'Metade do preço..........{metade(num)}')
        print(f'{diminuicao}% de redução...........{diminuir(num, diminuicao)}')
        print(f'{aumento}% de aumento...........{aumentar(num,aumento)}')
    print('=-'*20)
    