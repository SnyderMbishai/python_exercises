'''Write a program (function!) that takes a list 
and returns a new list that contains all the elements 
of the first list minus all the duplicates. '''

a=[8,5,4,7,7,8,8,9,9,6,2,1,8,7,4]

def remove_duplicates(x):
	x = set(x)
	x = list(x)
	print (x)

remove_duplicates(a)

#using loops
b=[4,6,6,7,7,8,8,8,8,9]
new_list = []
def remove_duplicates_loop(x):
	
	for i in x:
		if i not in new_list:
			new_list.append(i)

	return new_list

print(remove_duplicates_loop(b))