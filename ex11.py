print "What is your first name?",
nameF = raw_input()

print "What is your last name?",
nameL = raw_input()

print "How old are you?",
age = int(raw_input())

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "How many pets do you have?",
pets = int(raw_input())
print "What are their names?",
petNames = raw_input()

print "Where were you born?",
birthplace = raw_input()
print "What's your birthdate?",
birthdate = raw_input()

print "Hello, %s. Here are your details:" %(nameF)
print "%s %s" % (nameF, nameL)
print "You were born in %s on %r" % (birthplace, birthdate)
print "So %s, you're %d old, %s tall, and %s heavy." % (nameF, age, height, weight)
print "You have %d pets, and their names are %s" % (pets, petNames)


#comma after print line keeps my answer on teh same line
#and not a new line.