
def reverse_string():
	string = input("Write a sentence of your own choice: ")
	new_string = []
	string = string.split()
	l = len(string)-1
	for  i in string:
		new_string.append(string[l])
		l -= 1
	return (' '.join(new_string))


print(reverse_string())

#a simpler way

string2=input("sentence here: ")
print (' '.join( (string2.split()[::-1])))


