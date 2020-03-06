#Name- Tanubrata Dey
#Date- !9 March 2018
#This program prints: NYC Population

import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print("The largest number living in the Brooklyn is", pop["Brooklyn"].max())

print("The average number living in the Brooklyn is", pop["Brooklyn"].mean()) 

print("The largest number living in the Staten Island is", pop["Staten Island"].max())

print("The average number living in the Staten Island is", pop["Staten Island"].mean()) 

print("The largest number living in the Bronx is", pop["Bronx"].max())

print("The average number living in the Bronx is", pop["Bronx"].mean()) 

print("The largest number living in the Manhattan is", pop["Manhattan"].max())

print("The average number living in the Manhattan is", pop["Manhattan"].mean()) 
