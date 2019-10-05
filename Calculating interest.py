# For this code ive made an example of how to have someone generate $10,000 in an account based on interest, and it will tell you how much you need to deposit today to make that amount

future_value= float(input('Please enter the desired amount that you wish to generate: '))
# This part of the code is prompting a user on what the desired amount of money they would like to have at the end of the 10 years
interest_rate= float(input('Please enter the interest rate that is currently in effect: '))
# This part is a prompt to input the current interest rate that is in effect
years= int(input('How many years would you like for this to be generated over: '))
#The years part is an integer as i would prefer a whole number to make the maths easier and more coherent
present_value= future_value / (1.0 + interest_rate) ** years
#this part calculated the amount needed to deposit to get the future value
print('You will need to deposit the following amount to get that: ', present_value)
# Finally the printed value of the amount needed to deposit