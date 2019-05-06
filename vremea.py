import requests

oras = input("Introdu Orașul: ")
api = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=28cfde573f3c289f2551633d218f4e79&units=metric'.format(oras)
info = requests.get(api)
date = info.json()

try:
    temp = date['main']['temp']
    vitezaVantului = date['wind']['speed']
    latitudine = date['coord']['lat']
    longitudine = date['coord']['lon']
    descriere = date['weather'][0]['description']

    print('Temperatura:', int(temp), 'grade celsius')
    print('Viteza vantului: {}' .format(vitezaVantului))
    print('Latitudine: {}' .format(latitudine))
    print('Longitudine: {}' .format(longitudine))
    print('Descriere: {}' .format(descriere))
    
except:
    print("Oras inexistent sau scris gresit")
