words = ['Betty', 'girl', 'Fabian', 'dog', 'The George', 'dog']
otherWords = []

for each_word in words:
	if len(each_word) > 5:
		print each_word.upper()
	elif len(each_word) == 5:
		print each_word
	elif len(each_word)== 4:
		otherWords.append(each_word)
		print " ~boop~ "
	elif len(each_word) == 3:
		otherWords.append(each_word)
		print " ~poop"
	else: 
		print "Whaaaa?"

print otherWords