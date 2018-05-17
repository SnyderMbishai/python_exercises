import random 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list=[]

for x in b:
	if x in a and x not in new_list:
		new_list.append(x)
print (new_list)

#in one line of code
print([x for x in b if x in a])

#generating a random list

c=random.sample(range(1,20),5)
d=random.sample(range(2,40),6)
print(c)
print(d)