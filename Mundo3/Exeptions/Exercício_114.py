import urllib
import urllib.request


try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('\033[0;31m Não consegui acessar o site Pudim :(\033[0m')
else:
    print('Consegui acessar o site PUDIM')