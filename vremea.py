import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--oras', required=True, help="Seteaza orasul care sa fie cautat.")
    return parser.parse_args()


def main():
    #Nu inteleg nimic din ce am scris pe aici
    args = parse_args()
    api = f'http://api.openweathermap.org/data/2.5/weather?q={args.oras}&appid=28cfde573f3c289f2551633d218f4e79&units=metric'
    info = requests.get(api)
    date = info.json()
    try:
        temp = date['main']['temp']
        vitezaVantului = date['wind']['speed']
        latitudine = date['coord']['lat']
        longitudine = date['coord']['lon']
        descriere = date['weather'][0]['description']
        country = date['sys']['country']

        print('Temperatura:', int(temp), 'grade celsius')
        print('Viteza vantului: {}' .format(vitezaVantului))
        print('Latitudine: {}' .format(latitudine))
        print('Longitudine: {}' .format(longitudine))
        print('Descriere: {}' .format(descriere))
        print('Tara de origine: {}' .format(country))
    except:
        print("Oras scris incorect sau inexistent")
    

if __name__ == '__main__':
    main()
