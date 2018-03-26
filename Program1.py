#Program1
#1/23/2017
#This program accepts input from the user, then aproximates the square root of the number inputed by the user

again = 1

while again != 0:
	correct = 0
	D = int(input("Enter number to approximate the square root of: ")) #user input
	X = D #this is just used to initialize X
	counter = 0
	previousValue = D

	for I in range(1, 11):
		previousValue = X
		if I == 1:
			X = (1 + D/1)/2
		else:
			X = (X + D/X)/2
			
		if previousValue != X:
			counter = counter + 1
		
		print(X)


	print("After 10 approximations, the square root of ", D , " is: ", X)
	print("It took this algorithm ", counter, " computations to determine that answer")
	print("Would you like to enter another number? If Yes, submit 1. If no, submit 0")
	while correct == 0:
		again = input("Input here: ")
		if again == "1" or again == "0":
			if again == "0":
				again = int(0)
			if again == "1":
				again = int(1)
			correct = 1
		else:
			print("Please enter either 0 or 1.")
			print(" ")
			correct = 0

#Kody Kostboth
#D972C566