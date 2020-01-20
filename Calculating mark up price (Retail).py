#This program calculates retail prices.

MARK_UP = 2.5 #The markup percentage
another = 'y' #Variable to control the loop

#Proces one or more items

while another == 'y' or another == 'Y':
    wholesale = float(input("Enter the item's wholesale cost: "))

    #Calculate the retail price
    retail = wholesale * MARK_UP

    print('Retail price: $', format(retail, ',.2f'), sep='')

    another = input('Do you have another item?' + '(Enter Y for yes): ')
