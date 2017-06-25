shipping_cost = 2.5
prices = [3, 4, 5.25]
costs =[]
total = 0
line = "- " * 20

for price in prices:
	costs.append(price + shipping_cost)
	subttl = price + shipping_cost
	total = total + subttl
	print "price is " + str(price) + " plus " + str(shipping_cost)
	print "subtotal is " + str(subttl)
	print "running total is " +str(total)

	print line



print line

print prices
print costs
print total