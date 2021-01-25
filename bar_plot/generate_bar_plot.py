# bar plot

import numpy as np
import matplotlib.pyplot as plt


# creating data set
data ={ 'Česko': 7776, 'Belgie': 5849, 'Chorvatsko': 5497, 'Švédsko': 5007, 'VB': 4705, 'Španělsko': 4635, 'Rakousko': 4334, 'Itálie': 3842, 'Bulharsko': 3005, 'Estonsko': 2680}
per_capita = list(data.keys())
values = list(data.values())

# Creating the bar plot
plt.figure(figsize=(10,6))
plt.bar(per_capita, values, color = 'maroon', width = 0.4)

# label and title
plt.ylabel('Počet nakažených (ke dni 14.1.2021)', fontsize = 12)
plt.title('Kumulativní počet nakažených na 100 000 obyvatel ve vybraných zemích Evropy', fontsize = 16)

# zarovnani popisku
plt.tight_layout()

# saving plot
plt.savefig('bar_plot', dpi=200)
