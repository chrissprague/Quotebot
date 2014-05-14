"""
python project to accompany the /quote/ script
this file contains the functionality of reading from
and writing to the file containing user-input quotes.

for more info, including the README, issues, and
changelogs, see [[ https://github.com/chrissprague/Quotebot ]]

author: christopher sprague
"""

import random, sys, os # import statements

absolute_path = os.path.expanduser('~/bin/quotes') # reference to quotes file

def add_quote(string):
	"""
	take a quote (a string) and write it to the /quotes/ file.
	param: string: the quote to add (a string)
	"""
	with open (absolute_path, 'a') as f: f.write (string+"\n")
	print('Quote added: "'+string+'"')
	f.close()

def get_quote():
	"""
	randomly fetch a quote from the /quotes/ file.
	"""
	f = open(absolute_path,"r+")

	if not os.stat(absolute_path).st_size > 0 : # file is empty - cannot fetch any quotes
		print("Error: no quotes to grab!")
		return;

	# evaluate the number of lines, to give us upper bound on random
	num_lines = 0
	for line in f:
		num_lines+=1

	# pick a line randomly
	count = 0
	target = random.randint(0, num_lines+1)
	f.close()

	# reopen the file at the top/beginning
	f=open(absolute_path,"r+")

	for line in f:
		if count == target:
			if line == '' or line == '\n' or line == '\0':
				f.close()
				get_quote() # try again
			elif '\n' not in line:
				f.close()
				get_quote() # try again
			else:
				# quote we got was good, use it.
				print(line,end='')
				return;
		count+=1

	f.close()
	get_quote() # try again - we will exit the function when we hit a return();

if __name__ == "__main__":
	if len(sys.argv) > 2: # too many arguments
		print("Usage: quote [quote_to_add]")
		exit()

	if len(sys.argv) == 2: # add a quote
		add_quote((str)(sys.argv[1]))

	else: # read/fetch a quote
		get_quote()



