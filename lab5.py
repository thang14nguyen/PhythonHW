print('----- Lab 5 -----')
print()
print('----- Section C -----')


#Sectin C.1
'Define a Dish, include name, price, and number of calories'
import collections
Dish = collections.namedtuple('Dish', 'name price calories')

'Define three dishes'
d1 = Dish('Paht Woon Sen', 9.5, 330)
d2 = Dish('Brisket', 12, 400)
d3 = Dish('Fried Rice', 10.5, 650)
d4 = Dish('Paht Woon Sen', 12.5, 330)
d5 = Dish('Char Siu', 8, 450)


#Section C.2
'Function to print name, price, and calories'
def Dish_str(dish):
    msg = str(dish.name) + ' ($' + '{:.2f}'.format(round(dish.price,2)) + '): ' + str(dish.calories) + ' cal'
    return(msg)

assert Dish_str(d1) == 'Paht Woon Sen ($9.50): 330 cal'
print()
print()


#Section C.3
'Check to see if two dishes have the same price and calories'
def Dish_same(dish1, dish2):
    if dish1.name == dish2.name:
        if dish1.calories == dish2.calories:
            return(True)
        else:
            return(False)
    else:
        return(False)

assert Dish_same(d1, d2) == False
assert Dish_same(d1, d4) == True


#Section C.4
'Function for percentage change'
def percent_change(number, percent):
    change = number + (number*(percent/100))
    return(change)

assert percent_change(100, 20) == 120
assert percent_change(100, -30) == 70

'Function to change the price of a Dish'
def Dish_change_price(percent, dish):
    updated_price = percent_change(dish.price, percent)
    dish = Dish(dish.name, updated_price, dish.calories)
    return(dish)

assert Dish_change_price(10, d2) == Dish('Brisket', 13.2, 400)


#Section C.5
'Function to determine if price of a dish is lower than the stated number'
def Dish_is_cheap(price, dish):
    return(dish.price < price)

assert Dish_is_cheap(10, d1) == True
assert Dish_is_cheap(10, d2) == False


#Section C.6
DL = [d1, d2, d3, d4, d5]

DL2 =[Dish('Pizza', 4, 500),
      Dish('Mac n Cheese', 6, 450),
      Dish('Ribs', 7.75, 700),
      Dish('Chicken Nuggets', 5, 600)]

'Combine two list'
DL.extend(DL2)

'Print the list as one string'
def Dishlist_display(List):
    dish_name = ''
    for dish in List:
        dish_name = str(dish_name) + str(dish) + ' \n'
    print(dish_name)


#Section C.7
'Function to check if all dishs is less than the stated amount'
def Dish_all_cheap(price, List):
    for dish in List:
        if Dish_is_cheap(price, dish) == False:
            return (False)
            break
        else:
            return(True)

assert Dish_all_cheap(2, DL) == False
assert Dish_all_cheap(20, DL) == True
        

#Section C.8
'Function to change price of dish, and return the new list'
def Dishlist_change_price(percent, List):
    updated_price_list = []
    for dish in List:
        updated_dish = Dish_change_price(percent, dish)
        updated_price_list.append(updated_dish)
    return(updated_price_list)


#Section C.9
'Funtion to return all prices within a list as a list'
def Dishlist_price(List):
    dish_price = []
    for dish in List:
        dish_price.append(dish.price)
    return(dish_price)

#Section C.10
'Function to determine the average prices of dish within list'
def Dishlist_average(List):
    total_cost = 0
    for dish in List:
        total_cost = total_cost + dish.price
    average = total_cost / len(List)
    return(average)

#Section C.11
'Function that create a new list that keeps all dish that is less than stated price'
def Dishlist_keep_cheap(price, List):
    cheap_list = []
    for dish in List:
        if Dish_is_cheap(price, dish) == True:
            cheap_list.extend(dish)
    return(cheap_list)


#Section C.12
DL3 = [Dish('Noodles', 11, 800),
       Dish('Pho', 9.5, 775),
       Dish('Wontons', 3, 250),
       Dish('Dumplings', 10.5, 400),
       Dish('Kebab', 15, 560),
       Dish('Steak', 26, 600),
       Dish('Lobster', 40, 420),
       Dish('Surf n Turf', 55, 600)]

DL.extend(DL3)


def before_and_after():
    percent = float(input('Percent change: '))
    print()
    'Print original list'
    Dishlist_display(DL)
    print()
    'Create new list based on user percent input and print list'
    updated_list = Dishlist_change_price(percent, DL)
    Dishlist_display(updated_list)
    

print()
print('----- Section D -----')
print()



# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = [Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50),
                 Restaurant('Thai Princess', 'Thai', '01-11-22-33-44', 'Pad Thai', 15.50)] 
    our_rests = handle_commands(our_rests)    
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 c:  Change price for the dishes served
 p:  Print all the restaurants
 e:  Remove (erase) all the restaurant from the collection
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='c':
            p = int(input ("Please enter the percentage change in price:   "))
            C = Collection_change_prices(C, p)
        elif response=='e':
            C = Collection_new()
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")))


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result


def Collection_change_prices(C: list, percent: float) -> list:
    """ Given percentage, change all prices by that percent within collection.
    """
    updated_price = [] 
    for index in range(len(C)):
        current_r = C[index]        
        temp_price = current_r.price * (1 + (percent/100))
        temp_r = Restaurant(current_r.name, current_r.cuisine, current_r.phone, current_r.dish, temp_price)
        updated_price.append(temp_r)
    return updated_price
        
restaurants()


print()
print('----- Section E -----')
print()


Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
#Dish = collections.namedtuple('Dish', 'name price calories')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01',[Dish('Homard Bleu', 45.00, 750),
                                                          Dish('Tournedos Rossini', 65.00, 950),
                                                          Dish("Selle d'Agneau", 60.00, 850)])

#Section E.1
r3 = Restaurant('Pascal', 'French', '940-752-0107', [Dish('Escargots', 12.95, 250),
                                                     Dish('Salmon', 18.50, 550),
                                                     Dish('Lamb', 24.00, 850),
                                                     Dish('Marjolaine Cake', 8.50, 950)])

#Section E.2
r4 = Restaurant('Le Torch', 'French', '940-752-0107','')
current_restaurants = [r1, r2, r3, r4]
                
def Resturant_first_dish_name(name):
    for index in range(len(current_restaurants)):
        temp_r = current_restaurants[index]
        if name == temp_r.name and len(temp_r.menu)>0:
            return temp_r.menu[0].name
        elif name == temp_r.name and len(temp_r.menu)==0:
            return temp_r.menu
    

assert Resturant_first_dish_name('Thai Dishes') == 'Mee Krob'
assert Resturant_first_dish_name('Taillevent') == 'Homard Bleu'
assert Resturant_first_dish_name('Pascal') == 'Escargots'


#Section E.3
def Restaurant_is_cheap(name, price):
    for index in range(len(current_restaurants)):
        temp_r = current_restaurants[index]
        if name == temp_r.name and len(temp_r.menu)>0:
            return (Dishlist_average(temp_r.menu)<price)

assert Restaurant_is_cheap('Thai Dishes', 20) == True
assert Restaurant_is_cheap('Taillevent', 20) == False
assert Restaurant_is_cheap('Pascal', 20) == True
assert Restaurant_is_cheap('Le Torch', 20) == None


#Section E.4
def Collection_raise_prices(restaurant_list):
    temp_restaurant_list = []
    for index in range(len(restaurant_list)):
        current_r = restaurant_list[index]
        temp_r = Restaurant_raise_prices(current_r)
        temp_restaurant_list.append(temp_r)
    return temp_restaurant_list
    


def Restaurant_raise_prices(restaurant):
    menu = restaurant.menu
    #print(menu)
    temp_menu = Menu_raise_prices(menu)
    temp_restaurant = Restaurant(restaurant.name, restaurant.cuisine, restaurant.phone, temp_menu)
    return temp_restaurant


def Menu_raise_prices(menu):
    temp_menu = []
    for index in range(len(menu)):
        current_dish = menu[index]
        temp_dish = Dish_raise_prices(current_dish)
        #print(temp_dish)
        temp_menu.append(temp_dish)
    return temp_menu

def Dish_raise_prices(dish):
    temp_price = dish.price + 2.50
    temp_dish = Dish(dish.name, temp_price, dish.calories)
    return temp_dish


#Section E.5
def Collection_select_cheap(restaurant_list, price):
    cheap_restaurants = []
    for index in range(len(restaurant_list)):
        current_r = restaurant_list[index]
        if Restaurant_is_cheap(current_r.name, price) == True:
            #print(current_r)
            cheap_restaurants.append(current_r)
    return(cheap_restaurants)
            


#Section G

Count = namedtuple('Count', 'letter number')

def letter_count(some_message, letters):
    Letters = list(letters)
    print(Letters)
    letter_count = []
    for letter in Letters:
        temp_count = some_message.count(letter)
        temp_letter_count = Count(letter, temp_count)
        letter_count.append(temp_letter_count)
    return(letter_count)
        




