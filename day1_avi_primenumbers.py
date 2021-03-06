def all_primes(upto):
    for i in range(1,upto+1):
        if is_prime(i):
            print(str(i) + " is a prime number")
        else:
            print(str(i) + " is not a prime number")
	
def is_prime(n):
    if (n == 2 or n == 3): return True
    if (n % 2 == 0 or n < 2): return False
    # square root of n: n**0.5
    for i in range(3, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def ask_user_for_number():
	asking = True
	while asking:
		n = input("Please enter a positive number greater than 1: ")
		if n.isdigit() and int(n) > 1:
			all_primes(int(n))
			asking = False
			break
			
ask_user_for_number()		