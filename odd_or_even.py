def odd_or_even(number):
	number=int(input("Enter a number: "))



	if number%2 != 0:

		print(str(number) + " is an odd number")

	elif number%4==0 and number%2==0:
		print (str(number) + " is an even number and a multiple of 4")

	else:
		if number%2 == 0:
			print(str(number) + " is an even number")


			
def two_numbers(num,check):
	num=int(input("please enter another number to check: "))
	check=int(input("please enter a second number to check: "))

	if num%check==0:
		print(str(num) + " is a multiple of " + str(check))

	else:
		if num%check!=0:
			print(str(num) + "is not a multiple of" + str(check))

	






odd_or_even(20)
two_numbers(20,40)

