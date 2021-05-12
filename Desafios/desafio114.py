import urllib
import urllib.request
nome = str(input('Digite a pagina ' )) 
anddres = 'http://www.'+nome+'.com.br'
try:
    urllib.request.urlopen(anddres)
    print('Site localizado')
except:
    print(f'Não foi possivel localizar o site {anddres}')