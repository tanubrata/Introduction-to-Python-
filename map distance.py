#Name- Tanubrata Dey
#Date- 22 April 2018
#This program prints: Closest point

import pandas as pd

import folium

csvFile = input("Enter a file name: ")

mapNY = pd.read_csv(csvFile)

mapNYC = folium.Map(location=[41,-74], zoom_start=10)

for index,row in mapNY.interrows():
    x1 = row["Latitude"]
    y1 = row["Longitude"]
    newMarker = folium.Marker([x1, y1], popup="closest", icon=folium.Icon(color='red')).add_to(mapNYC)

x2 = float(input("Enter your latitude: "))
y2 = float(input("Enteryour longitude: "))

yourMarker = folium.Marker([x2, y2], popup="You are here", icon=folium.Icon(color='blue')).add_to(mapNYC)

distance = eval((x1-x2)2 + (y1-y2)2)

print(distance)

mapNYC.save(outfile=input('Enter a name: '))
