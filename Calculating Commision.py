#This program calculates sales commissions

#Create a variable to control the loop

keep_going = 'y'

#Calcualte a series of commissions
while keep_going == 'y':
    #get a sales persons sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    #calculate the commission
    commission = sales * comm_rate

    #display the commission
    print('The commission is $',
          format(commission, ',.2f'), sep=' ')

    #See if the user wants to do another one.
    keep_going = input('Do you want to calculate another commission (Enter y for yes): ')
