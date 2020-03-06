#Name- Tanubrata Dey
#Date- 15 April 2018
#This program prints: Collision map

import pandas as pd

import folium

csvFile = input("Enter a CSV File: ")

collisionMap = pd.read_csv(csvFile)

mapNYC = folium.Map(location=[40, -74])

for index,row in collisionMap.iterrows():
    
    lat = row["LATITUDE"]
    
    lon = row["LONGITUDE"]
    
    name = row["TIME"]
    
    newMarker = folium.Marker([lat, lon], popup=name).add_to(mapNYC)


mapNYC.save(outfile = input("Enter a name: "))

