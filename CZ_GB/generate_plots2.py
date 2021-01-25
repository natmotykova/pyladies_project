# CZ and GB, create plot with two curves

import matplotlib.pyplot as plt
from datetime import datetime

# dictionary for conversion of variables (velicina)
prevodnik = {
            'kumulativni_pocet_nakazenych': 'Kumulativní počet nakažených',
            }

# x, y for cz and eng
def create_plot(x_cz,y_cz,x_eng,y_eng, velicina, date_modified):
    '''
    x - vstupni data pro osu x (datum)
    y - vstupni data pro osu y
    velicina - typ grafu (lisi se podle veliciny/promenne)
    '''

    # vytvoreni noveho okna pro graf
    plt.figure(figsize=(10,6))

    # reformat date (for each country)
    x_reformated_cz = list()
    x_reformated_eng = list()
    for datum in x_cz:
        x_reformated_cz.append(datetime.strptime(datum,"%Y-%m-%d").strftime("%d.%m.%Y"))
    for datum in x_eng:
        x_reformated_eng.append(datetime.strptime(datum,"%Y-%m-%d").strftime("%d.%m.%Y"))

    # plotting the points
    plt.plot(x_reformated_cz, y_cz, linestyle='dashed', color='r', label='ČR')
    plt.plot(x_reformated_eng, y_eng, linestyle='dashed', color='b', label='VB')

    plt.legend()

    # change xticks to weeks
    # data co 14 dni; vytvari list skrze cyklus
    plt.xticks(range(0,len(x_reformated_cz),14), [x_reformated_cz[w] for w in range(0,len(x_reformated_cz),14)], rotation='90', fontsize = 10)

    # namig the x axis
    plt.xlabel('datum [14 dní]', fontsize = 12)

    # naming the y axis
    plt.ylabel(prevodnik[velicina], fontsize = 12)

    # giving a title to my graph
    plt.title('Srovnání vývoje epidemie koronaviru v ČR a VB', fontsize = 16)

    # fit everything to figure
    plt.tight_layout()

    # nastaveni mrizky (od urciteho data)
    plt.xlim([x_reformated_cz[0],x_reformated_cz[-1]])

    #grid
    plt.grid(True)

    # saving plots
    plot_name = velicina + '_chart_' + date_modified + '.png'
    plt.savefig(plot_name, dpi=200)

    print(f'Succesfully created {plot_name}')
