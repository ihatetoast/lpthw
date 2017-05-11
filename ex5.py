name = 'Katy Cassidy'
age = 48
height_inches=65
weight_pounds = 125
eyes = 'brown'
teeth = 'whiteish'
hair = 'red'
weight_kilos = weight_pounds*0.45359237001
height_centi = height_inches*2.54


print "Let's talk about me: %s." %name
print "I am %d inches tall." %height_inches
print "That's %dcm tall." %height_centi
print "I weigh %d pounds." %weight_pounds
print "That's %dkg." %weight_kilos
print "I have %s eyes and %s hair." %(eyes, hair)
print "My teeth are usually %s depending on the coffee." %teeth

print "If I add %d, %d, and %d, I'd get %d." %(age, height_inches, weight_pounds, age+height_inches+weight_pounds)

# Change all the variables so there is no my_ in front of each one. 
#Make sure you change the name everywhere, not just where you used = to set them.
#DONE

# Try to write some variables that convert the inches and pounds to centimeters and kilograms. 
#Do not just type in the measurements. Work out the math in Python.
#DONE

# Search online for all of the Python format characters.
# Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
print "I am percentage sign r leads to:"
print "I am %r inches tall." %height_inches#no change
print "Let's talk about me: %r." %name# includes the ' ' around my name.
print "I am percentage sign x leads to:"
print "I weigh %x pounds." %weight_pounds #I weigh 7d pounds
print "I weigh %X pounds." %weight_pounds #I weigh 7D pounds

#i can use % without variables
print "%(person)s weighs %(weight)02d pounds." %\
	{'person': "Katy", 'weight': 125}