def generateMachineNumber():
	pass


def userInput():
	""" ask the user to enter a number """
	num = int( input('Please, enter a number: ') )

	# while user enters a number out of interval [1,10]:
	# 	input('Please, enter number in [1,2]')

	while num<1 or num>10:
		num = int( input('Please, enter a number in [1,10]: ') )


	print(num)


def compareNumbers():
	pass



userInput();