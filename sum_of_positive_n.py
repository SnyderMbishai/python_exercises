"""Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n."""
 
def sum_of_positive_intergers():
    number = int(input("Please enter a number: "))
    total = 0
    for num in range(0,number+1):
        total += num
    print(total)

    #alternatively:
    # sum_a = (number*(number+1))/2
    # print(sum_a)

sum_of_positive_intergers()
