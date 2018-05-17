import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in set(a):
	if i in set(b):
		c.append(i)

print(c)

d = random.sample(range(20),10)
e = random.sample(range(21),11)
f = ([i for i in set(d) if i in set(e)])
g = ([i for i in random.sample(range(5),4) if i in random.sample(range(6),3)])

print (d)
print (e)
print (f)
print (g)