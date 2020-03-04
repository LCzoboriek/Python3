# Ive been asked to write a program that determines a cost for a painting job

# First i will write a global variable for the cost per hour of labour
# This will be in $
LABOUR = 35

def paint_job():
    print('Hello there, welcome to the Petes Paints, this program will run through a few steps for you to get a quote on the cost of the painting job will be')
    #firstly this is the variable for the price of the paint
    price_of_paint = float(input('Please enter the total cost of paint per gallon here: '))
    # Next i ask the user to input the total wall space needed for painting
    total_wall_space = float(input('Please now proceed to enter the total wall space that you would like to be painted: '))
    # Next i will calculate the amount of paint needed, for ever 112 feet of wall space it requires 1 gallon of paint
    amount_of_paint = total_wall_space / 112
    print('The number of gallons of paint required is as follows:',(format(amount_of_paint, '.2f')))
    # 1 Gallon of paint is equal to 8 hours of labour, so i use the previous variable to attain the labour cost
    hours_of_labour = amount_of_paint * 8
    print('The hours required labour wise is as follows:',(format(hours_of_labour, '.2f')))
    labor_charge = hours_of_labour * LABOUR
    print('The cost for this would be $'+(format(labor_charge, '.2f')))




paint_job()
