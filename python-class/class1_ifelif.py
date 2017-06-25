name = raw_input("Name: ")

if name == "Katy" or name == "katy":
	print "Hello, me!"
else:
	print "You are not me. Why are you on my computer?"


print "\n" * 3
print " - - - "
print "\n" * 3
print "It's your birthday!"
answer = raw_input("How old are you? ")
age = int(answer)

if age < 21:
	print "you may not have an alcoholic drink, but here's some juice."
else:
	print "print "
	drinkType = raw_input("Would you like wine, beer, or a cocktail?")
	if drinkType == "wine":
		print "Red or white?"
		wine = raw_input("> ")
		if wine == "red" or wine == "Red"
			print "Here's a shiraz."
	elif drinkType == "beer"
		print "Gross"
	elif drinkType == "a cocktail":
		print "How strong do you want it?"
		strength = raw_input("weak or strong")

	else: 
		print "Sorry, we don't have that."