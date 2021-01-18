# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

# Implement Restaurant as a namedtuple, collection as a list


##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = [r1, r2, r3] 
    our_rests = handle_commands(our_rests)    
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 f:  Search the collection for selected cuisine
 d:  Search the collection for selected dish
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
            Restaurant_str_dish(C)
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='c':
            p = int(input ("Please enter the percentage change in price:   "))
            C = Collection_change_prices(C, p)
        elif response=='e':
            C = Collection_new()
        elif response=='f':
            f = str(input ("Please enter the name of the cusine:    "))
            cuisine_match = cuisine_check(f, C)
            Restaurant_str_dish(cuisine_match)
        elif response=='d':
            d = str(input ("Please enter the name of the dish:     "))
            dish_match = dish_check_list(d, C)
            Restaurant_str_dish(dish_match)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish')
Dish = namedtuple('Dish', 'name price calories')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

##def Restaurant_str(self: Restaurant) -> str:
##    return (
##        "Name:     " + self.name + "\n" +
##        "Cuisine:  " + self.cuisine + "\n" +
##        "Phone:    " + self.phone + "\n" +
##        "Dish:     " + self.dish + "\n" +
##        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_str_dish(Restaurant) -> str:
    for index in range(len(Restaurant)):
        current = Restaurant[index]
        print("Name:     {}".format(current.name))
        print("Cuisine:  {}".format(current.cuisine))
        print("Phone:    {}".format(current.phone))
        for index in range(len(current.dish)):
            current_dish = current.dish[index]
            print("Dish:     {}".format(current_dish.name))
            print("Price:    {}".format(current_dish.price))
            print("Calories: {}".format(current_dish.calories))
        avg_p = avg_price(current)
        avg_c = avg_calories(current)
        print("Average price:  ${0:5.2f}.  Average calories:  {1:5.1f}\n\n".format(avg_p, avg_c))


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


def avg_price(restaurant):
    """Return the average price of dishes within a restaurant"""
    num_dish = len(restaurant.dish)
    total_dish = 0
    for index in range(len(restaurant.dish)):
        current_dish = restaurant.dish[index]
        total_dish = total_dish + current_dish.price
    avg_price = total_dish / num_dish
    return avg_price

def avg_calories(restaurant):
    """Return the average calories of dishes within a restaurant"""
    num_dish = len(restaurant.dish)
    total_dish = 0
    for index in range(len(restaurant.dish)):
        current_dish = restaurant.dish[index]
        total_dish = total_dish + current_dish.calories
    avg_calories = total_dish / num_dish
    return avg_calories


def cuisine_check(cuisine:str, restaurant:list):
    """Search list of resturants for matching cusine and return list of restaurants with matches"""
    match_cuisine = []
    for index in range(len(restaurant)):
        current = restaurant[index]
        if cuisine == current.cuisine:
            match_cuisine.append(current)
    return match_cuisine


def dish_check_list(dish:str, restaurant:list):
    """Search list of restaurant for matching dish, and return list of restaurants with matches"""
    match_dish = []
    match = 0
    for index in range(len(restaurant)):
        current_rest = restaurant[index]
        if dish_check(dish, current_rest):
            match_dish.append(current_rest)
    return match_dish

def dish_check(dish:str, restaurant):
    """Search a single restaurant for a match dish, return true or false"""
    match = 0
    for index in range(len(restaurant.dish)):
        current_dish = restaurant.dish[index]
        if dish in str(current_dish.name):
            match = match + 1
    return match > 0



#Test Variables


r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01',[Dish('Homard Bleu', 45.00, 750),
                                                          Dish('Tournedos Rossini', 65.00, 950),
                                                          Dish("Selle d'Agneau", 60.00, 850)])

r3 = Restaurant('Pascal', 'French', '940-752-0107', [Dish('Escargots', 12.95, 250),
                                                     Dish('Salmon', 18.50, 550),
                                                     Dish('Lamb', 24.00, 850),
                                                     Dish('Marjolaine Cake', 8.50, 950)])

test_list = [r1, r2, r3]

assert dish_check('Larb', r1)
assert dish_check('Lamb', r3)
assert dish_check('Selle', r2)

#restaurants()

