input_value = raw_input("enter a pos int: ")
user_number = int(input_value)

while user_number > 0:
	print "user number is " + str(user_number)
	print "the user number is still positive"
	user_number = user_number - 1
	print "- " * 20

print "User's number is no longer positive."