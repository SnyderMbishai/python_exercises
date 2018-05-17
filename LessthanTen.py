a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for number in a:
	if number<5:
		print (number)


#printing all numbers in a list

for number in a:
	if number<5:
		b.append(number)
print(b)

#one line python code
print ([number for number in a if number<5])

#asking for an input and returning numbers that are less than it
num=int(input("enter a number: "))

print ([number for number in a if number<num])

#or:

for number in a:
	if number<num:
	    print (number)
