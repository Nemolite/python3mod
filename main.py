from tkinter import *
import random
tk = Tk()
def click(event):
    while True:
        for i in range(16):
            color = random.choice(random_color)
            canva.itemconfig("ball"+str(i),fill=color)
            canva.update()
            canva.after(50)

def move_ball1():
    canva.move(ball1,5,0)
    if canva.coords(ball1)[2]<500:
        canva.after(50,move_ball1)


canva = Canvas(width=500,height=500)
canva.pack()

random_color=["red","blue","green"]

for i in range(16):
    color = random.choice(random_color)
    canva.create_oval(20+i*30,50,40+i*30,70,fill=color,tags="ball"+str(i))

canva.create_line(0,50,500,50)
canva.create_text(250,150,text='Нажми, для начала праздника',tags='start')
canva.tag_bind('start','<Button-1>',click)

ball1 = canva.create_oval(350,350,380,380,fill="red")
move_ball1()

tk.mainloop()