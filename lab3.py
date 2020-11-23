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
def print_even_numbers(number) -> list:
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
import tkinter # Load the library; do this just once per program
def create_square(x1, y1, length):
    #x1 = 100
    #y1 = 100
    #length = 100
    x2 = x1 + length
    y2 = y1 + length
    my_window = tkinter.Tk()    # Create the graphics window
    my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
    my_canvas.pack()            # Put the canvas into the window
    my_canvas.create_rectangle(x1, y1, x2, y2) # Draw orange line
    tkinter.mainloop()          # Combine all the elements and display the window

#Section C.7
def create_circle(x1, y1, length):
    #x1 = 100
    #y1 = 100
    #length = 100
    x2 = x1 + length
    y2 = y1 + length
    my_window = tkinter.Tk()    # Create the graphics window
    my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
    my_canvas.pack()            # Put the canvas into the window
    my_canvas.create_rectangle(x1, y1, x2, y2) # Draw orange line
    my_canvas.create_oval(x1, y1, x2, y2) # Draw orange line
    tkinter.mainloop()          # Combine all the elements and display the window

print()
print()
print('---------- Part (D) ----------')
print()

#Section D.1
#Ask Viet to confirm - errors with namedtuples
import collections     # If this line is in your file already, you don't need it again
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
    for restaurant in RC:
        if name == str(Restaurant.name):
            print(Restaurant.price)
        else :
            print('No restaurant found')
            print(str(Restaurant.name))

