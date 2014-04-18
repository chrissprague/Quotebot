import random
def add_quote(string):
	f = open("test", "r+")
	first_quote = True
	while ( True ) :
		if f.readline() == "":
			break
		first_quote = False
	if first_quote == True :
		string=(str)(string)
	else:
		string="\n"+(str)(string)
	f.write(string)
	f.close
def get_quote():
	f = open("~/bin/.quotes")
	num_lines = 0
	for line in f:
		num_lines+=1
	count = 0
	target = random.randInt(0, num_lines)
	for line in f:
		if count == target:
			print(line)
			return;
		count+=1
add_quote("HeWorld!")
