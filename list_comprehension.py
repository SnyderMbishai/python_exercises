a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list=[]
for x in a:
	if x%2==0:
		even_list.append(x)


#list comprehension
even_list=[x for x in a if x%2==0]
print (even_list)

#or

print([x for x in a if x%2==0])