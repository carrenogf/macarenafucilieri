import requests
from bs4 import BeautifulSoup
def dolar_scraping():
    url = requests.get('https://www.dolarhoy.com/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find_all('div', {'class': 'val'})
    titulos = ['Blue compra','Blue venta','Oficial compra','Oficial venta','Mep compra','Mep venta','CCL compra','CCL venta','Solidario']
    cotizaciones = []
    try:
      for i  in range(len(titulos)):
          key = titulos[i]
          value = result[i+2].text
          cotizaciones.append([key,value])
    except:
      cotizaciones = []
    return cotizaciones