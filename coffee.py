def make_coffee(options=''):
	ingredients = ['coffee', 'water', 'sugar']

	if options:
		ingredients.append(','.join(options))
		print("%s is preffered" % options)
	print("I'm going to make tasty coffee, follow closely!")
	print("put some coffee in your favorite cup")
	print("add hot water")
	print("add sugar if preffered")
	print("you may add milk as i am")
	print("stir constantly to mix it all well")
	coffee = "Tastiest Coffee"
	return coffee

def serve_coffee(coffee, person):
	print("voila! Your {}  {} ! \n enjoy!".format(coffee, person))

#for evans
s_coffee = make_coffee('sugar')
serve_coffee(s_coffee, 'evans')

#gibbs
g_coffee=make_coffee(options='sugar')
serve_coffee(s_coffee,'gibbs')