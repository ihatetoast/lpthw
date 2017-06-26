def add_ten(number):
	return number + 10

divider = '~' * 50

print "def add_ten(number)"

num = int(raw_input("Give me a number: "))

print "Your number is " + str(num)
print "your number plus 10 is: "
print add_ten(num)

print divider

#Deduct 32, then multiply by 5, then divide by 9

temp = int(raw_input("What is the temp: "))

def convFtoC(fahr):
	print ((fahr - 32) * 5) / 9
	return ((fahr - 32) * 5) / 9

print "def convFtoC(temp)"

fTemp = int(raw_input("Give me a number: "))
print "the temperature in Fahrenheit is " + str(fTemp)
print "the temperature converted to Celcius is "
print convFtoC(fTemp)

print divider