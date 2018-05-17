'''
Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''



def generate_fibonacchi():
	number=int(input("How many fibonacci numbers do you want generated? "))
	x = 1
	if number == 0:
		fibonacci = []
	elif number == 1:
		fibonacci = [1]
	elif number == 2:
		fibonacci = [1,1]
	elif number>2:
		fibonacci=[1,1]
		while x<(number-1):
			fibonacci.append(fibonacci[x]+fibonacci[x-1])
			x += 1
	return fibonacci

print(generate_fibonacchi())
