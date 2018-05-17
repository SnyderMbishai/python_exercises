#note:1 is not a divisor
#to get the right range, add one to the final number

number=int(input("enter a number: "))
num=range(2,number+1)
divisors=[]

for x in num:
	if number%x==0:
		divisors.append(x)

print(divisors)
