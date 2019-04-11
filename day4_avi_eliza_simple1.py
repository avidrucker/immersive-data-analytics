asking = True
while asking:
	answer = input("Good day. What is your problem? Enter your response here or Q to quit: ")

	print("You answered: '" + answer + "'")

	if str.lower(answer) == 'q' or str.lower(answer) == "i am feeling great":
		asking = False

print("Thanks, we're done!")