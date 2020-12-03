print()
print()
print('---------- Part (c) ----------')
print()

#Section C.1
def abbreviate(month) -> chr:
    'Return first three letters of the month'
    return(month[:3])

#Section C.2
def find_area_square(length) -> int:
    'Return the area of the square'
    area = length ** 2
    return(area)

#Section C.3
def find_area_circle(radius) -> float:
    'Return the area of the square'
    pie = 3.14159
    area = pie * (radius ** 2)
    return(area)

#Section C.4
def print_even_numbers(number):
    'Return even numbers' 
    for integer in number:
        if integer % 2 == 0:
            print(integer)

#Section C.5
def calculate_shipping(weight) -> float:
    'Calculate shipping cost based on weight'
    if weight < 2:
        cost = 2
    elif weight >= 10:
        cost = 5 + ( (weight-10) * 1.5)
    else :
        cost = 5
    return(cost)

#Section C.6
import tkinter 
def create_square(x1, y1, length):
    #x1 = 100
    #y1 = 100
    #length = 100
    x2 = x1 + length
    y2 = y1 + length
    my_window = tkinter.Tk()    
    my_canvas = tkinter.Canvas(my_window, width=500, height=500)  
    my_canvas.pack()           
    my_canvas.create_rectangle(x1, y1, x2, y2)
    tkinter.mainloop()         

#Section C.7
def create_circle(x1, y1, length):
    x2 = x1 + length
    y2 = y1 + length
    my_window = tkinter.Tk()    
    my_canvas = tkinter.Canvas(my_window, width=500, height=500) 
    my_canvas.pack()            
    my_canvas.create_rectangle(x1, y1, x2, y2) 
    my_canvas.create_oval(x1, y1, x2, y2) 
    tkinter.mainloop()       

print()
print()
print('---------- Part (D) ----------')
print()

#Section D.1
import collections
Restaurant = collections.namedtuple('Restaurant', ['name', 'cuisine', 'phone', 'dish', 'price'])
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [Restaurant('Thai Dishes', "Thai", "334-4433", "Mee Krob", 12.50),
      Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
      Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
      Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
      Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
      Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
      Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

def restaurant_price(name):
    for search in RC:
        if name == search.name:
            print(search.price)

#Section D.2
sorted_price = sorted(RC, key=lambda x: x.price)
for x in sorted_price:
    print(x)

#Section D.3
def costliest(RC):
    sorted_price = sorted(RC, key=lambda x: x.price, reverse=True)
    highest_cost_restaurant = sorted_price[0]
    name_of_highest = highest_cost_restaurant.name
    return(name_of_highest)

#Section D.4
#Same as above

print()
print()
print('---------- Part (D) ----------')
print()

#Section E.1
Book = collections.namedtuple('Book', 'author title genre year price instock')
BSI = [Book('John Smith', 'Laminate', 'Self-help', 1996, 20.50, 10),
       Book('George Washington', 'True Democracy', 'History', 1816, 15.00, 5),
       Book('James Bond', 'Spycraft', 'Thriller', 2002, 22, 2),
       Book('J.K Rowling', 'Harry Potter', 'Childrens', 2003, 20, 20),
       Book('Oprah', 'True Inner Strength', 'Self-help', 2005, 12, 8),
       Book('Edward Snowden', 'True Patriot', 'Technology', 2006, 14, 13)]

#Ask Viet what is typically used as the naming scheme for "X" (Book) to avoid confusion
print("--Section E.1--")
print()
for book in BSI:
    print(book.title)
print()
print()

#Section E.2
print("--Section E.2--")
print()
sorted_by_title = sorted(BSI, key = lambda x: x.title)
for book in sorted_by_title:
    print(book.title)
print()
print()

#Ask Viet. Nametuples are inmuttable. How would be performed?

#Section E.3  #Return to to question
##print("--Section E.3--")
##print()
##for x in BSI:
##    updated_price = float(x.price * 1.1)
##    x[-2] = updated_price
##    print(x)
##print()    
##for book in BSI:
##    print(book)
##print()
##print()

#Section E.4
print("--Section E.4--")
print()
for x in BSI:
    if 'Technology' in x.genre:
        print(x.title)
print()
print()

#Section E.5
print("--Section E.5--")
print()
'Create two new list, before or after 2k'
book_before_2k = []
book_after_2k = []
for x in BSI:
    if x.year < 2000:
        book_before_2k.append(x)
    else:
        book_after_2k.append(x)

'To determine which list has more books'
if len(book_before_2k) < len(book_after_2k):
    msg = "More titles 2000 or later. (" + str(len(book_after_2k)) + " vs. " + str(len(book_before_2k)) +")"
    print(msg)
else:
    msg = "More titles before 200. (" + str(len(book_before_2k)) + " vs. " + str(len(book_after_2k)) +")"
    print(msg)
print()
print()


#Section E.6
print("--Section E.6--")
print()
highest_value = 0
for x in BSI:
    if x.price * x.instock > highest_value:
        highest_title = x.title
for x in BSI:       
    if highest_title == x.title:
        inv_value = x.price * x.instock
        msg = 'The highest-inventory-value book is ' + x.title +' by ' + x.author + ' at a value of ' + str(inv_value) + '.'
        print(msg)
#Ask Viet how you index by title, then calculate inventory value.
#I imagine this code would take significantly longer with a larger database if using loop function.

print()
print()
print('---------- Part (F) ----------')
print()

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()
my_canvas = tkinter.Canvas(my_window, width=500, height=500)

def draw_face_outline(x1, y1):
    x2 = x1 + 300
    y2 = y1 + 300
    #my_canvas.create_oval(100, 100, 400, 400)
    my_canvas.pack() 
    my_canvas.create_oval(x1, y1, x2, y2)


def draw_eye(x1, y1):
    x2 = x1 + 50
    y2 = y1 + 50
    x3 = x2 + 50
    y3 = y2 + 100
    x4 = x1 + 200
    y4 = y1 + 50
    x5 = x1 + 250
    y5 = y1 + 150
    my_canvas.pack() 
    my_canvas.create_oval(x2, y2, x3, y3, fill='black')
    my_canvas.create_oval(x4, y4, x5, y5, fill='black')
    

def draw_nose(x1, y1):
    x2 = x1 + 150
    y2 = y1 + 150
    x3 = x1 + 100
    y3 = y1 + 200
    x4 = x1 + 200
    y4 = y1 + 200
    my_canvas.pack()
    my_canvas.create_polygon(x2, y2, x3, y3, x4, y4, x2, y2)
    

def draw_mouth(x1, y1):
    x2 = x1 + 50
    y2 = y1 + 175
    x3 = x1 + 250
    y3 = y1 + 275
    my_canvas.pack()
    my_canvas.create_arc(x2, y2, x3, y3, start = 0, extent = -180, fill ='black')


def draw_face(x1, y1):
    my_canvas.pack() 
    draw_face_outline(x1, y1)
    draw_eye(x1, y1)
    draw_nose(x1, y1)
    draw_mouth(x1, y1)
    tkinter.mainloop()

