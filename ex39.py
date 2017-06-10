# things = ['a', 'b', 'c', 'd']
# print "things is a list and the second item is things[1] and that is: "
# print things[1]

# things[1] = 'Q'
# print "I have written things[1] = 'Q'."
# print "Now what happens when I print things:"
# print things
# print "Q is now the second item/first index."
# print "b is not only not second, it is gwooooon"

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'New York': 'NY',
	'Michigan': 'MI',
	'Texas': 'TX',
	'Hawaii': 'HI',
	'Alabama': 'AL',
	'Alaska': 'AK',
	'Arizona': 'AZ',
	'Arkansas': 'AR',
	'California': 'CA',
	'Colorado': 'CO',
	'Connecticut': 'CT',
	'Delaware': 'DE'

}

# create a basic set of states and some citites in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Ann Arbor',
	'FL': 'Miami',
	'IA': 'Pella',
	'CT': 'New Haven',
	'AK': 'Fairbanks',
	'AZ': 'Tucsan',
	'CO': 'Durango',
}
capitals = {
	'CA': 'Sacramento',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
	'IA': 'Des Moines',
	'CT': 'Hartford',
	'AK': 'Juneaur',
	'AZ': 'Phoenix',
	'CO': 'Denver',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Salem'

#print out some cities
print '-' * 10
print "New York state has: ", cities['NY']
print "Oregon state has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is ", states['Michigan']
print "Florida's abbreviation is ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has ", cities[states['Michigan']]
print "Florida has ", cities[states['Florida']]


# print every state abbreviation
print '-' * 10

for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by sttate that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas"
# get a city with a default value
city = cities.get('TX', 'Does not exist!')
print "The city for the state TX is %s" % city


print states.items()
print cities.items()


























