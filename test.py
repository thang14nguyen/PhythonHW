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
