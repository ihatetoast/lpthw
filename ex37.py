ten_things = "Apples Oranges Crows Telephone Light Sugar"
print ten_things

print "Wait, there are  not 10 things in that list. I'll fix that."

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]#counts bck from start, so last on
print stuff.pop()#returns the last one
print ' '.join(stuff)
print '#'.join(stuff[3:5])#joined 4th item and the next one until BEFORE the 6th, so it was just 4 and f5