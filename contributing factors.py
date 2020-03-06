#Name- Tanubrata Dey
#Date- 15 April 2018
#This program prints: Contributing factors

import pandas as pd

csvFile = input("Enter a file: ")

dey = pd.read_csv(csvFile)

print(dey["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
print(dey["CONTRIBUTING FACTOR VEHICLE 2"].value_counts()[:3])
print(dey["CONTRIBUTING FACTOR VEHICLE 3"].value_counts()[:3])
