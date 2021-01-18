#Lab 6

#Section C

#Section C.1

def contains(word:str, check:str):
    """Check to see if the second string is in the first string"""
    return(check in word)

assert contains('banana', 'ana')
assert not contains('racecar', 'ck')


#Section C.2

def convert_punctuation(sentence:str):
    """Convert punctation into blanks"""
    punctuation = list('*?!:.,;')
    new_sentence = ''
    for character in sentence:
        if character in punctuation:
            character = ''
        new_sentence = new_sentence + character
    return new_sentence

assert convert_punctuation('***The ?! quick brown fox:  jumps over the lazy dog.') == 'The  quick brown fox  jumps over the lazy dog'


def sentence_stats(sentence:str):
    """Return the length of characters, length in word, average length of each work"""
    length_characters = len(sentence)
    new_sentence_list = convert_punctuation(sentence).split()
    length_word = len(new_sentence_list)
    total_character = 0
    for word in new_sentence_list:
        total_character = len(word) + total_character
    avg_character = total_character / length_word
    print("Character: {}\nWords: {}\nAverage word length: {}".format(length_characters, length_word, avg_character))


#Section C.3

def initials(name:str):
    """Return the initals of a name in uppercase"""
    name_list = name.split()
    initials = ''
    for name in name_list:
        initials = initials + name[0]
    return initials.upper()

assert initials('Bill Cody') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'
        
    
#Section D

#Section D.1
from random import randrange

def random_gen(length:int, spread_start:int, spread_end:int):
    """Return list of stated length of random numbers between the stated range"""
    random_list = []
    for index in range(length):
        random_number = randrange(spread_start,spread_end)
        random_list.append(random_number)
    return random_list


#Section D.2
def roll2dice():
    """Return the total of two dice throws"""
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    return dice1 + dice2

def roll2dice_list(length:int):
    """Return list of stated length of two dice throws"""
    dice_list = []
    for index in range(length):
        dicethrow = roll2dice()
        dice_list.append(dicethrow)
    return(dice_list)
    

#Section D.3
def distribution_of_roll(length:int):
    """Return a distribution report of 2 dice throws"""
    print("Distribution of dice rolls\n")
    dice_list = roll2dice_list(length)
    for index in range(2,13):
        count_dice = dice_list.count(index)
        percent_of_throws = count_dice / length * 100
        visual = '*' * count_dice
        message = "{0:2}: {1:4} ({2:4.1f}%)  {3:}".format(index, count_dice, percent_of_throws, visual)
        print(message)
    print('-----------------------------')
    print("     {0:} rolls".format(length))


#Section E

#Section E.1
alphabet = 'abcdefghijklmnopqrstuvwxyz'

test = "Four score and seven years ago, our fathers brought forth on"

def rotated_alphabet(key:int):
    """Rotate the alphabet based on the key"""
    if key > 25:
        key = key%25
    crypt_alphabet = alphabet[key:] + alphabet[0:key]
    return crypt_alphabet


def Caesar_encrypt(msg:str, key:int):
    """Encrypt a string based on key"""
    translation = msg.maketrans(alphabet, rotated_alphabet(key))
    return msg.translate(translation)


def Caesar_decrypt(msg:str, key:int):
    """Decrypt a string based on key"""
    translation = msg.maketrans(rotated_alphabet(key), alphabet)
    return msg.translate(translation)


#Section F

#Section F.1

text1 = ["Four score and seven years ago, our fathers brought forth on",
         "this continent a new nation, conceived in liberty and dedicated",
         "to the proposition that all men are created equal.  Now we are",
         "   engaged in a great 		civil war, testing whether that nation, or any",
         "nation so conceived and so dedicated, can long endure.        " ]

text2 = ["Four score and seven years ago, our fathers brought forth on",
         "this continent a new nation, conceived in liberty and dedicated",
         "to the proposition that all men are created equal.  Now we are",
         "   engaged in a great 		civil war, testing whether that nation, or any",
         "    ",
         "  ",
         "nation so conceived and so dedicated, can long endure.        " ]

def print_line_numbers(msg:list):
    """Add line numbers for a list of strings"""
    for index in range(len(msg)):
        print("{0:5}:  {1:}".format(index, msg[index]))
        
##Ask viet how to configure a variable length within format function.


#Section F.2
def stats(msg:list):
    lines = len(msg)
    empty_lines = check_empty_line(msg)
    avg_char_per_line = total_char(msg) / lines
    if empty_lines == 0:
        avg_char_per_non_empty = 0
    else:
        avg_char_per_non_empty = total_char(msg) / empty_lines
    print("{0:4}   lines in list\n{1:4}   empty lines\n{2:>6.1f} average characters per line\n {3:>5.1f} average characters per non-empty line".format(lines, empty_lines, avg_char_per_line, avg_char_per_non_empty))
    #Is there a better way to format this? I did a manual format based on spacing.


def empty_line(sentence:str):
    """Return true if string only has empty spaces"""
    empty_checker = 0
    for letter in sentence:
        if letter in alphabet:
            empty_checker = empty_checker + 1
    return empty_checker == 0

assert not empty_line('Thang')
assert empty_line('    ')


def check_empty_line(paragraph:list):
    """Returns the number of empty lines in a list of sentences"""
    empty_line_number = 0
    for sentence in paragraph:
        if empty_line(sentence):
            empty_line_number = empty_line_number + 1
    return empty_line_number

assert check_empty_line(text1) == 0
assert check_empty_line(text2) == 2


def total_char(paragraph:list):
    """Returns the total number of character in list"""
    total_char = 0
    for sentence in paragraph:
        char_count = len(sentence)
        total_char = total_char + char_count
    return total_char

test1 = ["Thang Nguyen",
         "     "]
assert total_char(test1) == 17


#Section F.3
def list_of_words(msg:list):
    """"Return a list of word using a list of string"""
    list_of_words = []
    for sentence in msg:
        no_punctuation = convert_punctuation(sentence)
        list_no_punctuation = no_punctuation.split()
        list_of_words.extend(list_no_punctuation)
    return list_of_words
