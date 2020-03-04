#The following program was an excersize to build a program that would take into account 3 price brands
# for tickets for a show, take input for the amount of tickets sold for each tier, then display the price
# oindividually gained from tickets and then the total mount


#global variables for the ticket prices
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10
#main function to take the inputs in and then assign them to variables to then be returned
def amount_of_tickets_sold():
    a = int(input('Please enter the amount of tickets for tier a that was sold: '))* CLASS_A
    b = int(input('Please enter the amount of tickets for tier b that was sold: '))* CLASS_B
    c = int(input('Please enter the amount of tickets for tier c that was sold: '))* CLASS_C
    print('The total amount of revenue for tier A sold was',a)
    print('The total amount of revenue for tier B sold was',b)
    print('The total amount of revenue for tier C sold was',c)
    print('The total amount of revenue generated for the event was', (a + b + c))
    return a, b, c

amount_of_tickets_sold()

# If i was to add things to this down the line i think the use of a list or dictionary would help condense the code down
# and get rid of the repetition to a certain extent, will revisit this after  that module is completed
