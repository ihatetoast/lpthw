q1 = raw_input("What day is it? ")
q2 = raw_input("What season is it? ")
q3 = raw_input("What is the temperature in Fahrenheit? ")
season = q2.lower()
dotw = q1.lower()
temp = int(q3)
#print dotw, season, temp

#saturday, sprint, temp above 65, k will plant flowers
def willKermitPlantFlowers(dotw, season, temp):
	if (dotw == "saturday") and (season == "spring") and (temp > 65):
		print "Kermit is planting!"
		return True
	else: 
		print "Kermit says 'No way! I'm lounging in the pond today.'"
		return False

#don't forget to call the bloody function		
willKermitPlantFlowers(dotw, season, temp)

