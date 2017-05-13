people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take a car."
elif cars < people: 
	print "We need to carpool."
else: 
	print "We can walk."

if trucks > cars:
	print "that's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else: 
	print "maybe we still can't decide."

if people  > trucks and trucks > cars:
	print "Alright, let's just take the trucks."
else:
	print "Fine. Let's stay home then."