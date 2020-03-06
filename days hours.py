#Name: Tanubrata Dey
#Date: Feb 27, 2018
#This program prints: Leftover days & hours



hours = float(input("Enter number of hours: "))

days = (hours // 24)
print("The number of days are", days)
leftover = (hours % 24)
print("The number of leftover hours are", leftover)
