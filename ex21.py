def add(a, b):
	print "ADDING %d + %d: " %(a, b)
	return a + b
def subtract(a, b):
	print "SUBTRACTING %d - %d: " %(a, b)
	return a - b
def multiply(a, b):
	print "MULTIPLY %d * %d: " %(a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d by  %d: " %(a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(40, 9)
height = subtract(69, 4)
weight = multiply(25, 5)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "I think that becomes -3001 but it was really: ", what