import random

def select_word(fname="/usr/share/dict/words"):
	words = []
	with open(fname) as f :
		for i in f :
			i = i.strip()
			if i.isalpha() and i.islower() and len(i) > 6 :
				words.append(i)
	return random.choice(words)

def check_letter_exist(x,word):
	if x in word:
		return True
	else:
		return False

def replace_letters(word, correctGuesses):
	x = ""
	if word!="":
		for i in word:
			if i in correctGuesses:
				x = x+i
			else:
				x = x+"*"
	return x

def check_word_found(word):
	if '*' in word:
		return False
	else:
		return True
		
def main():
	word = select_word() 
	chance = 10
	wrongGuesses = []
	correctGuesses = []
	while chance > 0:
		ss = replace_letters(word, correctGuesses)
		print ss
		if check_word_found(ss):
			break
		print "wrong guesses:",wrongGuesses
		print "Turns remining: %r"% (chance)
		while True:
			userInput = raw_input('Enter a guess:')
			if len(userInput) == 1:
				break
			else:
				print 'Please enter only one character'
		if check_letter_exist(userInput, word):
			correctGuesses.append(userInput)
			print "secret word contains %r" %(userInput)
		else:
			if check_letter_exist(userInput,wrongGuesses):
				print "You already tried %r"%(userInput)
			else:
				chance -= 1
				wrongGuesses.append(userInput)
				print "Sorry, The secret word doesn't contain %r"%(userInput)
	if(chance>0):
		print "Congratulations!!"
	else:
		print word
		print "Sorry, You've tried your every turns"
		
if __name__ == '__main__':
   main()
