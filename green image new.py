#Name: Tanubrata Dey
#Date: Feb 23, 2018
#This program loads an image, displays it, and then creates, displays,
#and saves a new image that has only the green channel displayed.

import matplotlib.pyplot as plt

import numpy as np
x = input("Enter name of the input file: ")
y = input("Enter name of the output file: ")
img = plt.imread(x)   
                       

img2 = img.copy()                 
img2[:,:,0] = 0          
img2[:,:,2] = 0          

            

plt.imsave(y, img2)


