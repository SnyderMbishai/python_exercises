"""In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places."""

# def bottle_deposit():
#     bottle_type = str(input("What is the size of the bottle? \n for 1ltr or less type small \n for morethan 1ltr type large"))
#     number_of_bottles = int(input("Enter the number of bottles ordered: "))
#     #$0.01 for small $0.25 for large
#     if bottle_type=="small":
#         deposit = 0.10*number_of_bottles
#         print("Your deposit will be ", "$", deposit)
#     else:
#         deposit = 0.25*number_of_bottles
#         print("Your deposit will be ", "$", deposit)

#alternatively:

def bottle_deposit():
    number_of_small_bottles = int(input("Number of small bottles (1ltr or less): "))
    number_of_large_bottles = int(input("Number of large bottles(more than 1ltre): "))
    
    deposit = (number_of_small_bottles*0.10) + (number_of_large_bottles*0.25)
    print ("Your deposit will be $%.2f"%deposit)
    # .2f formats the output to the nearest 2 decimal place
    
bottle_deposit()
    
