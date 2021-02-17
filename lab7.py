#Section C

#List of Files

surnames_file = 'surnames.txt'
male_file = 'malenames.txt'
female_file = 'femalenames.txt'

import re
import random

#Section C.1


def read_file(file:str, sep:str):
    """Reads a file, and convert to list based on listed seperators"""
    file_list = open(file).read()
    file_new_list = re.split(sep, file_list)
    open(file).close()
    return file_new_list


def convert_to_list(names:list, frequency: int):
    """Filter a list based on order (every 1, 2, etc on list)"""
    convert_list = []
    for index in range(len(names)):
        if index % frequency == 0:
            current = names[index]
            convert_list.append(current)
    return convert_list

def generate_surnames():
    """Generate a list of surnames based on text file"""
    surnames = read_file(surnames_file,'\t|\n')
    surnames_list = convert_to_list(surnames, 4)
    return surnames_list


def generate_names():
    """Generate a list of surnames based on text files"""
    m_names = read_file(male_file, '\t|\n')
    f_names = read_file(female_file, '\t|\n')
    m_names_list = convert_to_list(m_names, 4)
    f_names_list = convert_to_list(f_names, 4)
    names = []
    names.extend(m_names_list)
    names.extend(f_names_list)
    return(names)


def random_names(number_of_names: int):
    """Return a list of randomly generated name based on the specified number"""
    surnames_list = generate_surnames()
    names_list = generate_names()
    generated_list = []
    for index in range(number_of_names):
        random_surname = int(random.randrange(len(surnames_list)))
        random_name = int(random.randrange(len(names_list)))
        generated_name = names_list[random_name] + ' ' + surnames_list[random_surname]
        generated_list.append(generated_name)
    return generated_list
        
#Test Section
print( '---- Section C.1 ----\n')
print(random_names(3))
print('\n\n')


#Section D.1
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#From Lab 6
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

def get_word_list():
    """Get word list and convert to list of strings"""
    word_list = read_file('word_list.txt', '\n').lower()
    return word_list


#For current lab

def get_encrypted_msg():
    """Get encrypted message and convert to list of strings"""
    encrypted_msg = read_file('lab7_encrypted_msg.txt', '\n')
    converted_msg = []
    open('lab7_encrypted_msg.txt').close()
    return encrypted_msg

def get_word_list():
    """Get word list and convert to list of strings"""
    word_list = read_file('word_list.txt', '\n')
    converted_list = []
    for line in word_list:
        current_line = line.lower()
        converted_list.append(current_line)
    open('word_list.txt').close()
    return converted_list

def Caesar_break(msg:list):
    """Run through 26 combination of caesar encrypt to break code"""
    for index in range(26):                                                 #Attempt to decrypt first string in list
        current = index + 1
        word_list = get_word_list()
        possible_msg = Caesar_decrypt(msg[0], current)
        #print(possible_msg + ' ' + msg[0] + ' ' + str(current))
        msg_word_list = possible_msg.split()
        #print(msg_word_list)
        for index in range(len(msg_word_list)):                             #Check to see if words exist on word list
            current_word = msg_word_list[index].lower()
            check = 0
            if current_word in word_list:
                check = check + 1
        if check > 0:
            encrypt_key = 'Encrypt key is: ' + str(current) + '\n'          #If words exist, print decrypt message
            print(encrypt_key)
            for line in msg:
                current_msg = Caesar_decrypt(line, current)
                print(current_msg)
            break


#Test section
print('---- Section D.1 ----\n')
msg = get_encrypted_msg()
word_list = get_word_list()

Caesar_break(msg)
print('\n\n')

#Section E

#Section E.1
print('---- Section E.1 ----\n')


def copy_file():
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()

#Ask Viet about type of data is "infile". Based on the above, it works like a list
#due to for loop context but can't be manipulated as such.


def m_copy_file(cmd:str):
    """Modified version of copy file function for testing to copy and paste sherlock file"""
    infile_name = input("Please enter the name of the file to copy: ")
##    infile_name = 'Adventures_of_Sherlock_Holmes.txt'
    infile = open(infile_name, 'r', encoding='utf8')
    infile_str = infile.read()
    infile_list = infile_str.split(sep = '\n')
    outfile_name = input("Please enter the name of the new copy:  ")
##    outfile_name = "Adventures_of_Sherlock_Holmes_Copy.txt"
    outfile = open(outfile_name, 'w', encoding='utf8')
    if cmd == 'line numbers':
        passage_line_number = line_numbers(infile_list)
        outfile.write(passage_line_number)
    elif cmd == 'gutenberg trim':
        passage_trim = gutenberg_trim(infile_list)
        outfile.write(passage_trim)
    if cmd == 'statistics':
        passage_stats = statistics(infile_list)
        outfile.write(passage_stats)
    else:
        normal_passage = normal_print(infile_list)
        outfile.write(normal_passage)
    infile.close()
    outfile.close()

def line_numbers(str_list:list):
    """Take a list of strings, and return a string with line numbers"""
    char_width = len(str(len(str_list)))
    passage_line_number = ''
    for index in range(len(str_list)):
        current_line = str_list[index]
        line_number = index + 1
        line = "{0:{1}}:  {2}\n".format(line_number, char_width, current_line)
        passage_line_number = passage_line_number + line
    return passage_line_number

#print(line_numbers(["Thang", "is", "great!"]))


##def gutenberg_trim(str_list:list):
##    """Take a list of string, search for beginning and end of passage, and return the section as string"""
##    start_line = 0
##    end_line = 0
##    lst_length = len(str_list)
##    for index in range(lst_length):
##        current_line = str_list[index]
##        if "*** START" in current_line:
##            start_line = index + 1
##            break
##    for index in range(lst_length):
##        if "*** END" in current_line:
##            end_line = index + 1
##            break
##    print(start_line)        
##    print(end_line)        
##    passage_trim = normal_print(str_list[start_line:end_line])
##    return(passage_trim)

#Ask viet why the above doesnt work but below does.
#From my perspective, it appears to only breaking out the "check_str" function

def gutenberg_trim(str_list:list):
    """Take a list of string, search for beginning and end of passage, and return the section as string"""
    start_line = check_str("*** START", str_list)
    end_line = check_str("*** END", str_list) + 1
    print(start_line)
    print(end_line)
    passage_trim = str_list[start_line:end_line]
    print_trim = normal_print(passage_trim)
    return(print_trim)


def statistics(str_list:list):
    """Take list of string, reviews for stats, and return the states and list of string as string"""
    stats_str = stats(str_list)
    print_stats = normal_print(stats_str) + '\n\n' + normal_print(str_list)
    return(print_stats)    
    

#From Lab6 Work

def stats(msg:list):
    """Return stats from a list of string"""
    lines = len(msg)
    empty_lines = check_empty_line(msg)
    avg_char_per_line = total_char(msg) / lines
    if lines == 0:
        avg_char_per_non_empty = 0
    else:
        avg_char_per_non_empty = total_char(msg) / (lines - empty_lines)
    max_whole_int = len(str(max(lines, empty_lines, avg_char_per_line, avg_char_per_non_empty)))
    lines_str = "{0:{1}}   lines in list".format(lines, max_whole_int)
    empty_lines_str = "{0:{1}}   empty lines".format(empty_lines, max_whole_int)
    avg_char_per_line_str = "{0:{1}.1f} average characters per line".format(avg_char_per_line, max_whole_int+2)
    avg_char_per_non_empty_str = "{0:{1}.1f} average characters per non-empty line".format(avg_char_per_non_empty, max_whole_int+2)
    stats = [lines_str, empty_lines_str, avg_char_per_line_str, avg_char_per_non_empty_str]
    return stats


def empty_line(sentence:str):
    """Return true if string only has empty spaces"""
    empty_checker = 0
    for letter in sentence:
        if letter in alphabet:
            empty_checker = empty_checker + 1
    return empty_checker == 0



def check_empty_line(paragraph:list):
    """Returns the number of empty lines in a list of sentences"""
    empty_line_number = 0
    for sentence in paragraph:
        if empty_line(sentence):
            empty_line_number = empty_line_number + 1
    return empty_line_number


def total_char(paragraph:list):
    """Returns the total number of character in list"""
    total_char = 0
    for sentence in paragraph:
        char_count = len(sentence)
        total_char = total_char + char_count
    return total_char

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Lab7 Functions
def check_str(search_str:str, str_list:list):
    """Search for a string in a list, return index within list"""
    lst_length = len(str_list)
    found_index = 0
    for index in range(lst_length):
        current_line = str_list[index]
        if search_str in current_line:
            found_index = index
            break
    return found_index

def normal_print(str_list:list):
    """Take a list of strings, and return as a string"""
    current_line = ''
    passage_normal = ''
    for line in str_list:
        current_line = line + '\n'
        passage_normal = passage_normal + current_line
    return(passage_normal)

#Test
m_copy_file('line numbers')
m_copy_file('gutenberg trim')
m_copy_file('statistics')

