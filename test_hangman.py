import hangman

def test_select_word_avoid_bad():
	fname = "/tmp/test_dict.txt"
	f = open(fname, "w")
	f.writelines(["aa\n","Cccccccc\n","ewewq\n"])
	f.close()

	word = hangman.select_word(fname)

	assert word == ''

def test_select_word_select_good():
	fname = "/tmp/test_dict.txt"
	f = open(fname, "w")
	f.writelines(["aaa\n","Cccccccc\n","fg'ewewq\n","testabcdas\n"])
	f.close()

	word = hangman.select_word(fname)

	assert word == 'testabcdas'

def test_check_letter_exist_good():
    word = "word"
    x = "d"
    result = hangman.check_letter_exist(x,word)
    assert result == True 

def test_check_letter_exist_bad():
    word = "word"
    x = "m"
    result = hangman.check_letter_exist(x,word)
    assert result == False 

def test_replace_letters_good():
	correctGuesses = ['a','b']
	word = "aabbccaabbcc"
	secretword = hangman.replace_letters(word, correctGuesses)
	assert secretword == "aabb**aabb**"

def test_replace_letters_bad():
	correctGuesses = []
	word = "aabbccaabbcc"
	secretword = hangman.replace_letters(word, correctGuesses)
	assert secretword == "************"

def test_check_word_found_good()	:
	word = "afssgsg"
	assert hangman.check_word_found(word) == True

def test_check_word_found_bad()	:
	word = "afs**gsg"
	assert hangman.check_word_found(word) == False
	assert hangman.check_word_found('*****') == False