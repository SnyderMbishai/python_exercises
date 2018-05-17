import sys

user_1 = input("user one please provide your input: rock, paper or scissors?")
user_2 = input("user two please provide your name: rock, paper or scissors?")

while user_1=="rock":
	if user_2=="scissors":
		print("congratulations user_1, You win!")
	else:
		if user_2=="paper":
			print ("congratulations user_2, you win!")
			
while user_1=="scissors":
	if user_2=="paper":
		print("congratulations user_1, You win!")
	else:
		if user_2=="rock":
			print("congratulations user_2, You win!")
			

while user_1=="paper":
	if user_2=="rock":
		print("congratulations user_1, You win!")

	else:
	    if user_2=="scissors":
	    	print("congratulations user_2, You win!")
	    	

sys.exit()
