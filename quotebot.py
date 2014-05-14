import random, sys, os
absolute_path = os.path.expanduser('~/bin/quotes')
def add_quote(string):
	with open (absolute_path, 'a') as f: f.write (string+"\n")
	print('Quote added: "'+string+'"')
	f.close()
def get_quote():
	f = open(absolute_path,"r+")
	num_lines = 0
	for line in f:
		num_lines+=1
	count = 0
	target = random.randint(0, num_lines+1)
	f.close()
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
				print(line,end='')
				return;
		count+=1
	f.close()
	get_quote()
if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("Usage: quote [quote_to_add]")
		exit()
	if len(sys.argv) == 2:
		add_quote((str)(sys.argv[1]))
	else:
		get_quote()
