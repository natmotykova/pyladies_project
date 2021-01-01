# create plots

import matplotlib.pyplot as plt
from datetime import datetime

# dictionary for conversion of variables (velicina)
prevodnik = {
            'kumulativni_pocet_nakazenych': 'Kumulativní počet nakažených',
            'kumulativni_pocet_vylecenych': 'Kumulatnvní počet vyléčených',
            'kumulativni_pocet_umrti': 'Kumulativní počet úmrtí',
            'kumulativni_pocet_testu': 'Kumulativní počet testů',}


def create_plot(x,y, velicina, date_modified):
    '''
    x - vstupni data pro osu x (datum)
    y - vstupni data pro osu y
    velicina - typ grafu (lisi se podle veliciny/promenne)
    '''

    # vytvoreni noveho okna pro graf
    plt.figure(figsize=(10,6))

    # reformat date
    x_reformated = list()
    for datum in x:
        x_reformated.append(datetime.strptime(datum,"%Y-%m-%d").strftime("%d.%m.%Y"))  # datum oddeleno .

    # plotting the points
    plt.plot(x_reformated, y, linestyle='dashed', color='r')

    # change xticks to weeks
    # data co 14 dni,
    # vytvari se list skrze cyklus
    plt.xticks(range(0,len(x_reformated),14), [x_reformated[w] for w in range(0,len(x_reformated),14)], rotation='90', fontsize = 10)

    # namig the x axis
    plt.xlabel('datum [14 dní]', fontsize = 12)

    # naming the y axis
    plt.ylabel(prevodnik[velicina], fontsize = 12)

    # giving a title to my graph
    plt.title('Vývoj epidemie koronaviru v ČR', fontsize = 16)

    # fit everything to figure
    plt.tight_layout()

    # nastaveni mrizky (od jakeho data)
    plt.xlim([x_reformated[0],x_reformated[-1]])

    #grid
    plt.grid(True)

    # saving plots
    plt.savefig(velicina + '_chart_' + date_modified + '.png', dpi=200)
