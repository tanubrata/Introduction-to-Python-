#Name- Tanubrata Dey
#Date- 27 April 2018
#This program prints: non-empty string

string = input("Enter a non-empty string: ")

while string == "":
    print('That was empty. Try again.')
    string = input("Enter a non-empty string: ")
print("You entered: ", string)
