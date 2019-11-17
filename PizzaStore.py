#The start of the code is a stored variable of all the different kinds of pizzas that are sold in the store
toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']

#This variable is the prices of the pizzas
prices=[2,6,1,3,2,7,2]

#I then got a variable saved for specifying the amount of different pizzas that we sell
num_pizzas=len(toppings)

#I then wanted to find out what the cheapest pizza that we sold and make it easily callable in case the
#store owner wanted to find out what it was
cheapest_pizza=pizzas[:1]

#The same goes for the most expensive pizza that the store sells
priciest_pizza=pizzas[-1]

#I was then asked to save a variable what the three cheapest pizzas we sell for possibly making a pizza deal
three_cheapest=pizzas[:3]

print(three_cheapest)

#The store owner wanted to find out how many different pizzas we have are at 2 dollars
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
