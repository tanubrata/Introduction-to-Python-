#Name: Tanubrata Dey
#Date:Feb 26, 2018
#This program prints:Binary number to decimal

binString = input("Enter a binary number: ")

decNum = 0.
for c in binString:
    n = int(c)
    decNum = 2 * decNum + n
print(decNum)
