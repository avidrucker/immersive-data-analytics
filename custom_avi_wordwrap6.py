p_easy = "Yum yum yum yum yum yum yum yum sushi!"
p_med = "I eat cheese and bananas for breakfast."
p_hard = "Antidisestablishmentarianism is a word that is ridiculously long. It is sufficiently arduous to have discipline under such circumstances..."

MAX_LEN_1 = 12
MAX_LEN_2 = 24
MAX_LEN_3 = 36

p_list = p_hard.split()

# print(p_list)

# for each word, see if it goes beyond the bounds of the current line

def too_big(w, a):
	if len(w) > a:
		return True
	else:
		return False
	
tb_list = []
	
for word in p_list:
	tb_list.append(too_big(word, MAX_LEN_1))
	
# print(tb_list)

# these are the words that need to be cut down further OR they need their own line

# let's say that, for max 10 characters per line, we will show only full
# words if they aren't too big (only show if they fit perfectly, otherwise
# cut them up onto multiple lines)

big_word_list = []
for word in p_list:
	if too_big(word, MAX_LEN_1):
		big_word_list.append(word)
		
# print(big_word_list)

def big_word_to_chunks(word, width):
	temp = []
	for i in range(len(word)//width+1):
		if i == (len(word)//width+1)-1:
			temp.append(word[width*i:width*i+width])
		else:
			temp.append(word[width*i:width*i+width] + "-")
	return temp
	
# print(big_word_to_chunks("Antidisestablishmentarianism", MAX_LEN_1))
# this confirms we can cut words that are too big down

# so, let's look at our original list of words, p_list, and convert that whole list to words that can be rendered correctly for our line width

f_list = [] # formatted list
for word in p_list:
	if too_big(word, MAX_LEN_1):
		chunks = big_word_to_chunks(word, MAX_LEN_1)
		for chunk in chunks:
			f_list.append(chunk)
	else:
		f_list.append(word)

# how did we do? let's see:
#print(f_list)

# now we have a list of words that are at most the max line width,
# and never any higher. we can now build lines that are made of such
# words, though we can see already that there won't be any joinings
# between words have been cut up (with a hyphen, for example)

def build_paragraph(arrIn, width):
	temp = ""
	left = width
	for item in arrIn:
		if left < 2:
			temp += "\n"
			left = width
		elif left == width:
			#print("...passing...")
			pass
		else:
			temp += " "
			left -= 1
	
		if len(item) <= left: 
			temp += item
			left -= len(item)
		else:
			# does temp end with a newline?
			if temp!= "" and temp[-1] != "\n":
				temp += "\n" #if not, we add one here
			temp += item
			left = width - len(item)
			
		#print("left is " + str(left) + " after '" + item + "'")
	return temp		

# let's try feeding in our formatted list 'f_list' to 'build_paragraph()'
#print(build_paragraph(f_list,MAX_LEN_1))
# looking good. let's test it now on different passages with different widths

# text to take in
# width to format it to
def format_text(t, w):
	#1: split & cut down each word
	t_list = []
	for word in t.split():
		if too_big(word, w):
			chunks = big_word_to_chunks(word, w)
			for chunk in chunks:
				t_list.append(chunk)
		else:
			t_list.append(word)
	#2: build a paragraph from the list
	return build_paragraph(t_list, w)

print("\noriginal: " + p_easy)
print("\nwrapped to " + str(MAX_LEN_1) + " chars:")
print(format_text(p_easy, MAX_LEN_1))
print("\noriginal: " + p_med)
print("\nwrapped to " + str(MAX_LEN_1) + " chars:")
print(format_text(p_med, MAX_LEN_1))
print("\noriginal: " + p_hard)
print("\nwrapped to " + str(MAX_LEN_1) + " chars:")
print(format_text(p_hard, MAX_LEN_1))
print("\nwrapped to " + str(MAX_LEN_2) + " chars:")
print(format_text(p_hard, MAX_LEN_2))
print("\nwrapped to " + str(MAX_LEN_3) + " chars:")
print(format_text(p_hard, MAX_LEN_3))