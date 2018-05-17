'''Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first 
and last elements of the given list.
For practice, write this code inside a function.'''

a = [2,6,8,10,11,22]

def print_last_and_first(x):
	print([x[0], x[len(x)-1]])


print_last_and_first(a)