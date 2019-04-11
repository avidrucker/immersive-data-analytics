asking = True
while asking:
	answer = input("ELIZA: Good day. What is your problem? Enter your response here or Q to quit: ")

	print("'" + answer + "'")

	mod_answer = answer.replace(".","")
	answer_list = mod_answer.split()

	print(answer_list)

	modified5 = ""
	for word in answer_list:
		if word == "I":
			modified5 += "you"
		elif str.lower(word) == "me":
			modified5 += "you"
		elif str.lower(word) == "my":
			modified5 += "your"
		elif str.lower(word) == "am":
			modified5 += "are"
		else:
			modified5 += word
		modified5 += " " # after every word, add a space

	modified6 = modified5[:-1] # remove trailing space

	if str.lower(answer) == 'q' or str.lower(answer) == "i am feeling great":
		# we break the loop to quit the program
		asking = False
	else:
		# therapist says
		print("ELIZA: Why do you say that " + modified6 + "?")

print("ELIZA: Thanks, we're done!")