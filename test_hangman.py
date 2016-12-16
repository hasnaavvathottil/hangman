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

