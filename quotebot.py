import random
import sys
def add_quote(string):
	f = open("quotes", "r+")
	first_quote = True
	original = string
	while ( True ) :
		if f.readline() == "":
			break
		first_quote = False
	if first_quote == True :
		string=(str)(string)
	else:
		string="\n"+(str)(string)
	f.write(string)
	print('Quote added: "'+original+'"')
	f.close()
def get_quote():
	f = open("quotes","r+")
	num_lines = 0
	for line in f:
		num_lines+=1
	count = 0
	target = random.randint(0, num_lines)
	f.close()
	f=open("quotes","r+")
	for line in f:
		if count == target:
			if line == '' or line == '\n' or line == '\0':
				get_quote() # try again
			elif '\n' not in line:
				get_quote() # try again
			else:
				print(line,end='')
				return;
		count+=1
	f.close()
	get_quote()
if len(sys.argv) > 2:
	exit()
if len(sys.argv) == 2:
	add_quote((str)(sys.argv[1]))
else:
	get_quote()
