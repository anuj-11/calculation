try:
	val1 = input('Please enter the first value: ')
	val2 = input('Please enter the second value: ')
	operation = raw_input("Please type in the math operation you would like to perform: ")
	if operation == '+':
		print(val1 + val2)
	elif operation == '-':
		print(val1 - val2)
	elif operation == '*':
		print(val1 * val2)
	elif operation == '/':
		print(val1 / val2)
	else:
		raise ValueError
except ArithmeticError:
	print("invalid input")
except ValueError:
	print("enter only mathematical operation")
