#This program displays a property taxes

TAX_FACTOR = 0.0065

#Get the first lot number
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))

#Continue processing as long as the user does not enter lot number 0
while lot != 0:
    value = float(input('Enter the property value here: '))

    #Calculate the propertys tax
    tax = value * TAX_FACTOR

    #Display the tax
    print('Property tax: $', format(tax, ',.2f'), sep=' ')

    #Get the next lot number
    print('Enter the property lot number')
    print('or enter 0 to end.')
    lot = int(input('Lot number: '))
