#Name- Tanubrata Dey
#Date- 8 April 2018
#This program prints: Parking ticket

import pandas as pd

csvFile = input('Enter CSV file name: ')         
tickets = pd.read_csv(csvFile)     
attribute = input("Enter name of attribute: ")
print(tickets[attribute].value_counts()[:10])

