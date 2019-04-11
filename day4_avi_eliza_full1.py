import random

replace_dict = {
	"i":"you",
	"me":"you",
	"my":"your",
	"am":"are"
}

def strip_punc(s):
	if s[-1] == "?" or s[-1] == "!" or s[-1] == ".":
		return s[:-1]
	else:
		return s

def mirror_sen(s):
	# initialize temp string & lower the cases
	temp = str.lower(s)
	
	# split temp string into a list
	temp_list = temp.split()
	
	# initialize memory for rebuilt string
	new_str = ""
	
	# replace the words in the replace list
	for word in temp_list:
		if word in replace_dict:
			new_str += replace_dict.get(word)
		else:
			new_str += word
		new_str += " " # add space after each word
		
	return new_str[:-1] # take off that last space, we don't need it

sen_list = ["I like cheese.","I smell the roses.","I am happy.","I didn't like my last meal."]	
	
"""print(mirror_sen(sen_list[0]))
print(mirror_sen(sen_list[1]))
print(mirror_sen(sen_list[2]))
print(mirror_sen(sen_list[3]))"""

hedges = ["Please tell me more.","Many of my patients tell me the same thing.", "It is getting late, maybe we had better quit... Please type 'Q' whenever you're ready *cough* *cough*"]
qualifiers = ["Why do you say that ", "You seem to think that ", "So, you are concerned that "]

def greet():
	print("Hello there, what's on your mind? Please type your reponse here or Q to quit: ")
	
def listen():
	return input()
	
def ready_to_quit(s):
	if str.lower(s) == "i am feeling great" or str.lower(s) == "q":
		return True
	else:
		return False

def say_bye():
	print("I'm glad we could meet today. I hope the rest of your day goes great!")
		
def answer(s):
	num = random.randrange(6)
	if num > 2:
		print(hedges[num-3])
	else:
		print(qualifiers[num] + mirror_sen(s) + "?")
		
def start_session():
	greet() # greet_person
	in_session = True
	while in_session:
		said = strip_punc(listen()) # person_said, listen_to_person
		if ready_to_quit(said):
			say_bye() # say_bye_to_person
			in_session = False
		else:
			answer(said) # answer_person

def main():
	random.seed()
	start_session()
	
if __name__== "__main__":
  main()