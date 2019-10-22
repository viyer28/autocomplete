
## constants ##


# Instruction: Write a function called function1 that, for 0 through 9, 
# prints out "even" if it's even and "odd" if it's odd.

def function1():
	for i in range(0, 10):
		if i % 2 == 0:
			print("even")
		else:
			print("odd")


# Instruction: Write a function called function2 that, for 0 through 19, 
# prints "yes" if its a multiple of 10, and "no" otherwise.

def function2():
	for i in range(0, 20):
		if i % 10:
			print("yes")
		else:
			print("no")


# Instruction: Write a function called function3 that, for 0 through 9, 
# prints "." for numbers less than 9, otherwise print "nine" 

def function3():
	for i in range(0, 9):
		if i < 9:
			print(".")
		else:
			print("nine")


# Instruction: Write a function called function4 that, for 0 through 11, prints
# out multiples of 3

def function4():
	for i in range(0, 12):
		if i % 3 == 0:
			print(i)
		else:
			pass


# Instruction: Write a function called function5 that for 0 through 4, 
# prints "*" for 0, and "#" otherwise

def function5():
	for i in range(0, 5):
		if i == 0:
			print("*")
		else:
			print("#")


function1()
function2()
function3()
function4()
function5()


