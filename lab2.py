#Section C
print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)

#Section C.1
hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour:  ', rate)
print('Weekly salary:  $', hours * rate)

#Section C.2
name = str(input('Hello. What is your name?'))
print('Hello, ' + name)
print("It's nice to meet you.")     #Ask Viet if there's a difference between "" and ''. Appears to be "" is used to be all inclusive
age = int(input('How old are you? '))
age_nextyr = age + 1
print('Next year you will be ' + str(age_nextyr) + ' years old')
print('Good-bye!')

#Section D

#Input[business_name, euros, pounds, usd]
#Output[business_name, euros_krone, pounds_krone, usd_krone, total]
# 1 euro -> 7.46 krone
# 1 pound -> 8.60 krone
# 1 usd -> 6.62 krone

print('Please provide this information:')
business_name = str(input('Business Name: '))
euro = float(input('Number of Euros: '))
pound = float(input('Number of Pounds: '))
usd = float(input('Number of Dollars: '))
euro_to_krone = 7.46
pound_to_krone = 8.6
usd_to_krone = 6.62

print('Copenhagen Chamber of Commerce')
print('Business Name: ' + business_name)
euro_convert = euro * euro_to_krone
print(str(euro) + ' euros is ' + str(euro_convert) + ' krone')
pound_convert = pound * pound_to_krone
print(str(pound) + ' pounds is ' + str(pound_convert) + ' krone')
usd_convert = usd * usd_to_krone
print(str(usd) + ' USD is ' + str(usd_convert) + ' krone')
total = euro_convert + pound_convert + usd_convert
print('Total krone:   ' + str(total))

#Section E
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')  #Ask Viet how this works. Doesn't it need to broken apart (X, X, X)
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

#Section E.1
print(another.author)

#Section E.2
print(another.price)

#Section E.3
#--------------------------------------------------

#Section E.4
print(favorite.year < 1900)

#Section E.5
still_another_price = 26.0
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, still_another_price)
print(still_another.price)

#Section E.6
still_another_price = still_another.price * 1.2
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, still_another_price)
print(still_another.price)

#Section F
from collections import namedtuple
animal = namedtuple('animal', 'name species age weight favorite_food')
jumbo = animal('Jumbo', 'elephant', 50, 1000, 'peanuts')
perry = animal('Perry', 'platypus', 7, 1.7, 'shrimp')
print(jumbo.weight < perry.weight)

#Section G
booklist = [favorite, another, still_another]

#Section G.1
print(booklist[0].price < booklist[1].price)

#Section G.2
print(booklist[0].year > booklist[-1].year)

#Section H
from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

#Section H.1
print(RC[2].name)

#Section H.2
print(RC[0].cuisine == RC[3].cuisine)

#Section H.3
print(RC[-1].price)

#Section H.4
for name in RC:
    print(Restaurant.name) #ask about errors

#Section H.5
sorted_dish = sorted(RC, key=lambda Resturant: Resturant.dish) #ask about various keys
print(sorted_dish)

#Section H.6
sorted_name = sorted(RC, key=lambda Resturant: Resturant.name)
new_list = [sorted_name[0], sorted_name[1], sorted_name[-2], sorted_name[-2]]
print(new_list)

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

#Section 1.1
my_canvas.create_line(100, 100, 100, 300, fill='orange') # Draw orange line
my_canvas.create_line(100, 300, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 300, 300, 100, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 100, 100, fill='orange') # Draw orange line

#Section I.2
my_canvas.create_line(200, 100, 300, 200, fill='orange') # Draw orange line
my_canvas.create_line(300, 200, 200, 300, fill='orange') # Draw orange line
my_canvas.create_line(200, 300, 100, 200, fill='orange') # Draw orange line
my_canvas.create_line(100, 200, 200, 100, fill='orange') # Draw orange line

tkinter.mainloop()          # Combine all the elements and display the window

#Section I.Rest - Didn't do. Understand the concepts but took forever to figure out position to complete house



