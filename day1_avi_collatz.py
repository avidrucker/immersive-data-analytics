def collatz(n):
	current = n
	temp = ""
	working = True
	while working:
		temp += str(current)
		# Do (the things below) until you get to 1 (base case)
		if current == 1:
			working = False
			break
		# Divide the number by 2 if it is even
		elif current % 2 == 0:
			current = int(current/2)
		# Multiply the number by 3, and add 1 if it is odd. 
		elif current % 2 == 1:
			current *= 3
			current += 1
		temp += " "
	return temp
	
print(collatz(5))
print(collatz(3))
print(collatz(12))