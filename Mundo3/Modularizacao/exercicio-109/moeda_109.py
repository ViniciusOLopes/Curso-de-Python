def aumentar(num=0,p=0,formatado=False):
    """Aumenta um valor em um determinado percentual.

    Args:
        num (int, float): O valor numérico inicial.
        p (int, float): A porcentagem do aumento (ex: 10 para 10%).
        formatado (bool): Se True, retorna o valor formatado como moeda.

    Returns:
        float, str: O valor aumentado. Retorna str se formatado=True, senão float.
    """
    
    if formatado:
        num = num*(1+(p/100))
        return moeda(num)
    return num*(1+(p/100))


def diminuir(num=0,p=0,formatado=False):
    """Diminui um valor em um determinado percentual.

    Args:
        num (int, float): O valor numérico inicial.
        p (int, float): A porcentagem do desconto (ex: 10 para 10%).
        formatado (bool): Se True, retorna o valor formatado como moeda.

    Returns:
        float, str: O valor reduzido. Retorna str se formatado=True, senão float.
    """
    
    if formatado:
        num = num*(100-p)/100
        return moeda(num)
    return num*(100-p)/100


def dobro(num=0,formatado=False):
    """Calcula o dobro de um número.

    Args:
        num (int, float): O número a ser dobrado.
        formatado (bool): Se True, retorna o valor formatado como moeda.

    Returns:
        int, float, str: O dobro do número. Retorna str se formatado=True.
    """
    
    if formatado:
        num = num*2
        return moeda(num)
    return num * 2


def metade(num=0,formatado=False):
    """Calcula a metade de um número.

    Args:
        num (int, float): O número a ser dividido por dois.
        formatado (bool): Se True, retorna o valor formatado como moeda.

    Returns:
        float, str: A metade do número. Retorna str se formatado=True.
    """
    
    if formatado:
        num = num/2
        return moeda(num)
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

