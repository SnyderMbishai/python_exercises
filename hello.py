"""Write a program that asks the user to enter his or her name. The program should
respond with a message that says hello to the user, using his or her name."""
def hello():
    name = input("What's your name? ")
    return("hello " + name)

print(hello())
    