import requests

import sys

url = "http://data.fixer.io/api/latest?access_key=b6fdba4588215d3b7456a728d8f7b17f&format=1"

birinci_doviz = input("Birinci Döviz:")
ikinci_doviz = input("İkinci Döviz:")
miktar = float(input("Miktar:"))



response = requests.get(url + birinci_doviz)

json_verisi = response.json()

try:
    print(json_verisi["rates"][ikinci_doviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen sikiklik yapma!")
    sys.stderr.flush()