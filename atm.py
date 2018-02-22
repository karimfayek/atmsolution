def atm(x , y):
	'''This function take tow argument balance and requested money '''
	if x > y:

		hundre = y /100
		print "give100\n" * hundre
		gived =  hundre*100
		rest1 = y - gived
		fifteen = rest1 /50
		print "give50\n" * fifteen
		gived2 = fifteen * 50
		rest2 = y - (gived + gived2 )
		ten = rest2 / 10
		print "give 10\n" * ten
		gived3 = ten * 10
		rest3 = y - (gived + gived2 + gived3)
		one = rest3 / 1
		print "give 1\n" * one 
	else:
		print " no Balance"



atm(520 , 600)