import random

numberToGuess = random.randint(1, 100)
print numberToGuess

user_number = int(raw_input("Enter a number between 1 and 100: "))
while user_number != numberToGuess:
	if user_number >100 or user_number < 1:
			print "You didn't follow directions! Please try again."
			user_number = int(raw_input("Enter a number between 1 and 100: "))
	elif user_number < numberToGuess:
			print "You picked " + str(user_number) + ". That is too low."
			user_number = int(raw_input("MAAAAAMP! Enter another numer number. This time higher: "))
	else:
			print "You picked " + str(user_number) + ". That is too high."
			user_number = int(raw_input("MAAAAAMP! Enter another numer number. This time lower: "))
		

	

print "Game over."
