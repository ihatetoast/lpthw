def high_and_low(numbers):
  numInt = []
  maxMin = []
  for num in numbers.split():
    numInt.append(int(num))
  maxMin.extend([str(max(numInt)), str(min(numInt))])


# best of submitted:
def high_and_low(numbers): #z.
				#nn is integer if number in string that is now a list of strings
    nn = [int(s) for s in numbers.split(" ")]
    #formatter using max mind
    return "%i %i" % (max(nn),min(nn))