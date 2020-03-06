#Name- Tanubrata Dey
#Date- 16 April 2018
#This program prints- LIRR transit fare

def computeFare(zone, ticketType):

    fare = 0

    if zone == 1:
        if ticketType == ("peak"):
            return (8.75)
        elif ticketType == ("off-peak"):
            return (6.25)

    elif zone == 2:
        if ticketType == ("peak"):
            return (10.25)
        elif ticketType == ("off-peak"):
            return (7.50)

    elif zone == 3:
        if ticketType == ("peak"):
            return (10.25)
        elif ticketType == ("off-peak"):
            return (7.50)

    elif zone == 4:
        if ticketType == ("peak"):
            return (12.00)
        elif ticketType == ("off-peak"):
            return (8.75)

    elif zone == 5:
        if ticketType == ("peak"):
            return (13.50)
        elif ticketType == ("off-peak"):
            return (9.75)

    elif zone == 6:
        if ticketType == ("peak"):
            return (13.50)
        elif ticketType == ("off-peak"):
            return (9.75)

    elif zone == 7:
        if ticketType == ("peak"):
            return (13.50)
        elif ticketType == ("off-peak"):
            return (9.75)

    elif zone > 8:
        return (-1)
     
     

    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print(fare)

#Allow script to be run directly:
if __name__ == "__main__":
    main()
