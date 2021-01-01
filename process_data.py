# Upload data

import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
from generate_plots import create_plot


# seznam odkazu (kumulativni pocet nakazenych = celkovy pocet nakazenych)
list_of_urls = ['https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakazeni-vyleceni-umrti-testy.json',
                'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/testy.json',
                'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakaza.json',
                'https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/nakazeni-vyleceni-umrti-testy.json']

datum_start = '2020-03-01'      # pocatecni datum v grafu


def get_data(url):
    '''
    Funkce pro nacteni url a konverzi do jsonu
    '''
    data = requests.get(url)   # data Mz
    data.raise_for_status()

    print(f'Succesfully uploaded data from {url}')  # pro kontrolu nacteni dat

    # Konverze z textoveho JSON formatu na Pythoni objekt
    json_data = json.loads(data.text)

    return json_data

# mozno pridat v cyklu nacteni dat
# for url in list_of_urls:
#    json_data = get_data(url)


json_data = get_data(list_of_urls[0])   # pozice dat, bere dle cisla


# datum aktualizace json souoru na webu
date_modified = json_data['modified']
#print(date_modified)

# Vypis dat
#print(json_data['modified'])

# seznam_pripady = list()
seznam_datum = list()
seznam_kumulativni_pocet = list()
seznam_kumulativni_pocet_vylecenych = list()
seznam_kumulativni_pocet_umrti = list()
seznam_kumulativni_pocet_testu = list ()

for radek in json_data['data']:
    #print(radek)
    seznam_kumulativni_pocet.append(radek['kumulativni_pocet_nakazenych'])
    seznam_kumulativni_pocet_vylecenych.append(radek['kumulativni_pocet_vylecenych'])
    seznam_kumulativni_pocet_umrti.append(radek['kumulativni_pocet_umrti'])
    seznam_kumulativni_pocet_testu.append(radek['kumulativni_pocet_testu'])
    seznam_datum.append(radek['datum'])
#print(seznam_pripady, seznam_datum)

# starting date
index_datum = seznam_datum.index(datum_start)
# print('Zaciname od data {} s pozici {}'.format(datum_start, seznam_kumulativni_pocet[index_datum]))


create_plot(seznam_datum[index_datum:], seznam_kumulativni_pocet[index_datum:], 'kumulativni_pocet_nakazenych', date_modified) 
create_plot(seznam_datum[index_datum:], seznam_kumulativni_pocet_vylecenych[index_datum:], 'kumulativni_pocet_vylecenych', date_modified)
create_plot(seznam_datum[index_datum:], seznam_kumulativni_pocet_umrti[index_datum:], 'kumulativni_pocet_umrti', date_modified)
create_plot(seznam_datum[index_datum:], seznam_kumulativni_pocet_testu[index_datum:], 'kumulativni_pocet_testu', date_modified)
