import time
import requests
from pygame import mixer

url = 'https://api.currencyfreaks.com/latest?apikey=40ca016a37054e2393b0983dca74e83d'
response = requests.get(url)
data = response.json()

kur1 = data["rates"]["TRY"]
kur1

mixer.init()
artis = mixer.Sound('ses.mp3')
azalis = mixer.Sound('ses2.mp3')


x = 0
while True:
    response = requests.get(url)
    data = response.json()
    kur2 = data["rates"]["TRY"]
    print("Eski Kur: {}".format(kur1))
    print("Güncel Kur: {}".format(kur2))
    x += 1
    print("{}. Tur".format(x))

    if kur2 > kur1:
        print("Kur Arttı")
        artis.play()
        
    elif kur2 == kur1:
        print("Kur Sabit")
    
    elif kur2 < kur1:
        print("Kur Düştü")
        azalis.play()
    
    kur1 = kur2

    time.sleep(14400)
