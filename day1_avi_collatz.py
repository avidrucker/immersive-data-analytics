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
	
def ask_user_for_number():
	asking = True
	while asking:
		n = input("Please enter a positive number greater than 1: ")
		if n.isdigit() and int(n) > 1:
			print(collatz(int(n)))
			asking = False
			break

def ask_user_to_continue():
	asking = True
	a = ""
	while asking:
		a = input("Another? Type 'y' for yes, 'n' for no: ")
		if a == 'y' or a == 'n':
			asking = False
			break
	return a
			
def __main__():
	running = True
	while running:
		ask_user_for_number()
		if ask_user_to_continue() == 'n':
			running = False
			break
	print("Buh-bye!")
	
__main__()