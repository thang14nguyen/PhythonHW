print('-----Section C------')
print()
print()

#Section C.1
#Realized there is a cleaner way to write this later on in the lab (Section D)
def num_even(x):
    if x % 2 == 0:
        attribute = True
    else:
        attribute = False
    return(attribute)

    
def num_odd(x):
    if x % 2 != 0:
        attribute = True
    else:
        attribute = False
    return(attribute)

def num_positive(x):
    if x >= 0:
        attribute = True
    else:
        attribute = False
    return(attribute)

def num_negative(x):
    if x < 0:
        attribute = True
    else:
        attribute = False
    return(attribute)

def test_number(x, test):
    if test == 'even':
       return(num_even(x))
    elif test == 'odd':
        return(num_odd(x))
    elif test == 'positive':
        return(num_positive(x))
    elif test == 'negative':
        return(num_negative(x))

assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

#Section C.2
def display():
    word = input('Enter a word: ')
    for letters in word:
        print(letters)

#Section C.3
def square_list(numbers):
    for integer in numbers:
        print(integer ** 2)

#Section C.4
def match_first_letter(letter, character):
    for x in character:
        if letter == x[0]:
            print(x)


char_list = ["Iron Man", 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend']

#Section C.5
def match_area_code(area_code, phone_number):
    for x in area_code:
        for y in phone_number:
            if x == y[1:4]:
                print(y)
                
area_code = ['714', '949']
phone_list = ['(714)824-1234', '(419)312-8732', '(949)555-1234']


#Section C.6
def match_area_codes(area_code, phone_number):
    phone_numbers = []
    for x in area_code:
        for y in phone_number:
            if x == y[1:4]:
                phone_numbers.append(y)
    print(phone_numbers)

print('-----Section D-----')
print()
print()

#Section D.1
def is_vowel(letter):
    vowels = list('aeiouAEIOU')
    return(letter in vowels)

assert not is_vowel('X')
assert not is_vowel('?')

#Section D.2
def print_nonvowels(word):
    for letter in word:
        if is_vowel(letter) == False:
            print(letter)
    
#Section D.3
def nonvowels(word):
    result = ''
    for letter in word:
        if is_vowel(letter) == False:
            result = result + letter
    return(result)

assert nonvowels('Thang') == 'Thng'
assert nonvowels('Nguyen') == 'Ngyn'
            
#Section D.4
def consonants(word):
    result = ''
    consonants = list('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    for letter in word:
        if letter in consonants:
            result = result + letter
    return(result)

assert consonants('Thang!') == 'Thng'
assert consonants('Nguyen!') == 'Ngyn'

#Section D.5
def vowels(word):
    result = ''
    for letter in word:
        if is_vowel(letter) == True:
            result = result + letter
    return(result)

def select_letters(character, word):
    if character == 'v':
        return(vowels(word))
    elif character == 'c':
        return(consonants(word))

assert select_letters('v', 'facetiously') == 'aeiou'
assert select_letters('c', 'facetiously') == 'fctsly'


#Section D.6
def hide_vowels(word):
    result = ''
    for letter in word:
        if is_vowel(letter) == True:
            result = result + '-'
        else:
            result = result + letter
    return(result)

assert hide_vowels('The cat in the hat wore no pants') == 'Th- c-t -n th- h-t w-r- n- p-nts'
            
print('-----Section E-----')
print()
print()

#Ask viet about replace values in a namedtuple, same issue as Lab3

from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

print('-----Section F-----')
print()
print()

#Section F.1
def alphabetical(List):
    sorted_list = sorted(List, key=lambda x: x.name)
    return(sorted_list)

#Section F.2
def alphabetical_name(List):
    sorted_list = alphabetical(List)
    names = []
    for restaurant in sorted_list:
        names.append(restaurant.name)
    return(names)

#Section F.3
def all_thai(List):
    thai = []
    for restaurant in List:
        if restaurant.cuisine == 'Thai':
            thai.append(restaurant)
    return(thai)

#Section F.4
def select_cuisine(cuisine, List):
    cuisine_list = []
    for restaurant in List:
        if restaurant.cuisine == cuisine:
            cuisine_list.append(restaurant)
    return cuisine_list

#Section F.5
def select_cheaper (price, List):
    price_list = []
    for restaurant in List:
        if restaurant.price < price:
            price_list.append(restaurant)
    return price_list

#Section F.6
#Ask Viet is this proper way to declare an interger variable
#How to return only two decimal points? Tried using round function but returns one decimal place
def average_price(List) -> float:
    total_price = 0
    for restaurants in List:
        total_price = total_price + restaurants.price
    #average_price = total_price / len(List)
    average_price = round((total_price / len(List)),2)
    return(average_price)

#Section F.7
def avgprice_indian(List):
    indian_restaurants = select_cuisine('Indian', List)
    print(average_price(indian_restaurants))

#Section F.8
def avgprice_Chinese_Thai(List):
    chinese_restaurants = select_cuisine('Chinese', List)
    thai_restaurants = select_cuisine('Thai', List)
    combine_restaurants = chinese_restaurants + thai_restaurants
    print(average_price(combine_restaurants))


#Section F.9
def print_cheaper(List):
    cheaper_list = select_cheaper(15, List)
    print(alphabetical_name(cheaper_list))


