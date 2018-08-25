import requests
from pprint import pprint

oras = input('Introdu orasul : ')

kelvin = '272.15'

api = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=28cfde573f3c289f2551633d218f4e79'.format(oras)

info = requests.get(api)

date = info.json()

temp = date['main']['temp']
viteza_vantului = date['wind']['speed']

latitudine = date['coord']['lat']
longitudine = date['coord']['lon']

descriere = date['weather'][0]['description']

#print('Temperatura: ', temp)
print('Temperatura: ', float(temp)-float(kelvin), 'grade celsius')
print('Viteza vantului: , {}' .format(viteza_vantului))
print('Latitudine: {}' .format(latitudine))
print('Longitudine: {}' .format(longitudine))
print('Descriere: {}' .format(descriere))


#print(float(temp)-float(kelvin))
