#more use of functions
def break_words(stuff):
    words = stuff.split(" ")
    """
    #while using some code editors like atom(which i am using) that has a feature to automaticaly
    close opend colon which caused a problem while using split method,
    as it takes the given string as a  single string
    """
    return words

def sort_words(words):
    "sorting the words"
    return sorted(words)

def print_first_word(words):
    'print_first_word'
    words = words.pop(0)
    return words

def print_last_word(words):
    "print_last_word"
    words =words.pop(-1)
    return words

def sort_sentence(sentence):
    """takes full sentence and sort into words"""
    word = break_word(sentence)
    return sort_words(words)

def print_first_and_last_(sentence):
    words = break_word(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
