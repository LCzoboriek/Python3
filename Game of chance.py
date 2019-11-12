import random

money = 100

#Functions for the actual game are here
def coin_flip(guess, bet):
  side = random.randint(1, 2)
  if guess == "Heads" and side == 1:
        total_money = int(money) + int(bet)
        print(int(bet))
        print("Heads, you won! Your total money is now " + str(money - int(bet)))
        return total_money
  if guess == "Tails" and side == 2:

        total_money = int(money) + int(bet)
        print(int(bet))
        print("Tails, you won! Your total money is now " + str(money + int(bet)))
        return total_money
  else:
      total_money = int(money) + int(bet)
      print(int(bet))
      print("You lost! Your total is now " + str(money - int(bet)))
      return total_money


# Game functions are called here
print(coin_flip(input("What side of the coin would you like to guess? "),input("How much would you like to bet? ")))