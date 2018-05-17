import random

alphabet = ['abcdefghijklmnopABCDEFGHIJKLMNOPQRSTUVWXYZ']
numbers = [0,1,2,3,4,5,6,7,8,9]
words = ['one', 'nun', 'red', 'black', 'voo']
symbols = ['#', '%', '@', '!']

def generate_password():

	password = str(random.sample(numbers,2))+(random.choice(words)) + (random.choice(alphabet))
	print (password)
generate_password()	
