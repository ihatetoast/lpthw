from sys import argv

def cheese_and_crackers(cheese_ct, boxes_crackers):
	print "You have %d cheeses." % cheese_ct
	print "You have %d boxes of crackers." % boxes_crackers
	print "You have enough for your party."


print "We can give function numbers directly: "
cheese_and_crackers(10, 30)

print "Or we can use variables: "
amt_of_cheese = 10
amt_of_crackers = 50

cheese_and_crackers(amt_of_cheese, amt_of_crackers)

print "And we can do the math in the args and with the args:"

cheese_and_crackers(amt_of_cheese *3, amt_of_crackers*2)


print '{}, {}, {}'.format('a', 'b', 'c')