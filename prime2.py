number = int(input('please enter a number: '))
x = [a for a in range(2,number) if number%a==0]

if number > 2:
	if len(x)>0:
		print('not prime')
	else:
		print('is prime')
else:
	print("not prime")