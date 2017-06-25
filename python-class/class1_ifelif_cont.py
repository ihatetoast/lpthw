health = 49
strHealth = str(health)

print "A vicious warg is chasing you."
print "Options:"
print "1 - hide in the cave"
print "2 - Climb a tree"

input_value = raw_input("Enter choice: ")
if input_value == "1":
	print "You hide in a cave."
	print "The warg finds you and injures your leg with his claws."
	health = health - 7
	strHealth = str(health)
elif input_value == "2":
	print "You climb a tree"
	print "The warg eventually loses interest and wanders off"
	health = health * 1.5
	strHealth = str(health)
else:
	print "You can't follow directions."
	health = health / health
	strHealth = str(health)

if health == 1:
	print "Your health is " + strHealth + "."
	print "You should just stop."
elif health > 50:
	print "You are smokin' with a health of " + strHealth + "."
else:
	print "Keep playing."