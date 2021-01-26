# Upload data, CZ and UK, per capita


import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from generate_plots2 import create_plot


# seznam odkazu (kumulativni pocet nakazenych = celkovy pocet nakazenych)
list_of_urls = ['https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakazeni-vyleceni-umrti-testy.json',
                'https://coronavirus.data.gov.uk/api/v1/data?filters=areaName=United%2520Kingdom;areaType=overview&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newCasesByPublishDate%22:%22newCasesByPublishDate%22,%22cumCasesByPublishDate%22:%22cumCasesByPublishDate%22%7D&format=json']


def get_data(url):
    '''
    Funkce pro nacteni url a konverzi do jsonu
    '''
    data = requests.get(url)
    data.raise_for_status()

    print(f'Succesfully uploaded data from {url}')  # pro kontrolu nacteni dat

    # Konverze z textoveho JSON formatu na Pythoni objekt
    json_data = json.loads(data.text)

    return json_data

def parse_json_cz(json_data):
    seznam_datum = list()
    seznam_kumulativni_pocet = list()

# vezme si danou promennou z json souboru
    for radek in json_data['data']:     # klic data obsahuje vsechny hodnoty
        #print(radek)
        seznam_kumulativni_pocet.append(radek['kumulativni_pocet_nakazenych'])
        seznam_datum.append(radek['datum'])

    return seznam_kumulativni_pocet, seznam_datum

def parse_json_uk(json_data):
    seznam_datum= list()
    seznam_kumulativni_pocet= list()

    for radek in json_data['data']:     # klic data obsahuje vsechny hodnoty
        #print(radek)
        seznam_kumulativni_pocet.append(radek['cumCasesByPublishDate'])
        seznam_datum.append(radek['date'])

    # switch retrospective to chrological order (i.e., transpose lists)
    seznam_kumulativni_pocet.reverse()
    seznam_datum.reverse()

    return seznam_kumulativni_pocet, seznam_datum

# nacteni dat
for url in list_of_urls:
    print(url)
    json_data = get_data(url)
    if '.cz' in url:
        seznam_kumulativni_pocet_cz, seznam_datum_cz = parse_json_cz(json_data)
    elif '.gov.uk' in url:
        seznam_kumulativni_pocet_eng, seznam_datum_eng = parse_json_uk(json_data)

#print(type(seznam_kumulativni_pocet))
#print(seznam_kumulativni_pocet[:10], seznam_datum[:10])

# datum aktualizace json souboru na webu, v nazvu grafu
date_modified = seznam_datum_cz[-1]
#print(date_modified)

# Vypis dat
#print(json_data['modified'])

# prepocet poctu obyvatel (na 100000 obyvatel)
cr_pocet_obyvatel = 10690000
vb_pocet_obyvatel = 66650000

per_capita_cz = (np.array(seznam_kumulativni_pocet_cz)/ cr_pocet_obyvatel) * 100000
seznam_kumulativni_pocet_eng = seznam_kumulativni_pocet_eng[28:]    # kvuli None v datech - potreba od teto pozice
seznam_datum_eng_cropped = seznam_datum_eng[28:]
per_capita_eng = np.divide(np.array(seznam_kumulativni_pocet_eng),vb_pocet_obyvatel) * 100000

per_capita_cz.tolist()
per_capita_eng.tolist()


create_plot(seznam_datum_cz, per_capita_cz, seznam_datum_eng_cropped, per_capita_eng, 'kumulativni_pocet_nakazenych', date_modified)
