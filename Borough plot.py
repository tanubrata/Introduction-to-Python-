#Name: Tanubrata Dey
#Date: 14 March 2018
#This program prints:Borough fraction plot

import matplotlib.pyplot as plt

import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)

pop['Fraction'] = pop['Queens']/pop['Total']

pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()

fig.savefig('queens.png')
