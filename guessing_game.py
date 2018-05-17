import random
import sys

c = 0
number = random.randint(1,9)
guess = 0

while number!=guess and guess!="exit":
        guess=int(input("guess a number btn 1 and 9, (type exit to exit): "))
        c += 1

        if guess=="exit":
                sys.exit()
        elif guess < number:
                print ("your guess is too low")
        elif guess > number:
                print("your guess is too high")
        else:
                print("you guessed right!")
        print("you guesed %s times" % c)










      
      















