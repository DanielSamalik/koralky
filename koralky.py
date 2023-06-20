import tkinter as tk
import random

w = 600
h = 500
farby = ["red", "green", "blue", "yellow"]
pocet = 10
velkost = 45
list1 = []
list2 = []
zaciatok = 100
zoz = []

def setup():
    global list1
    for i in range(40):
        x = random.randrange(0, w - velkost)
        y = random.randrange(0, h - velkost * 3)
        list1.append(canvas.create_oval(x, y, x + velkost, y + velkost, fill=farby[i // 10]))
    canvas.create_rectangle(0, h - 20, w, h-15, fill="black")

def control(event):
    global list2, list1, zoz
    zoznam_prvkov = canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
    if len(zoznam_prvkov) != 0 and zoznam_prvkov[0] in list1:
        if len(list2) == 0 and len(zoz) < 10:
            list2.append(zoznam_prvkov[0])
            zoz.append(zoznam_prvkov[0])
            list1.remove(zoznam_prvkov[0])
            print("Kliknuté!")
    moveit()

def moveit():
    global list2
    if len(list2) != 0:
        suradnice_lopty = canvas.coords(list2[0])
        konecna_pozicia = (w - velkost // 2, (h - velkost // 2)+30)
        dx = w - suradnice_lopty[2]
        dy = konecna_pozicia[1] - suradnice_lopty[3]
        if dx > dy and dy != 0:
            dx = dx / dy
            dy = 1
        elif dx < dy and dx != 0:
            dy = dy / dx
            dx = 1
        canvas.move(list2[0], dx, dy)
        if suradnice_lopty[2] == w:
            nit()
    canvas.after(10, moveit)

def nit():
    global zaciatok, list2
    if len(list2) != 0:
        suradnice_lopty = canvas.coords(list2[0])
        if suradnice_lopty[0] > zaciatok:
            canvas.move(list2[0], -1, 0)
            canvas.after(3, nit)
        else:
            zaciatok += velkost
            list2 = []

win = tk.Tk()

canvas = tk.Canvas(win, width=w, height=h, bg="white")
canvas.bind("<Button-1>", control)
canvas.pack()

setup()

win.mainloop()
