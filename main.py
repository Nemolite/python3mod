
import random
from tkinter import *
from tkinter import messagebox
tk = Tk()
def click(event):
    while True:
        for i in range(16):
            color = random.choice(random_color)
            canva.itemconfig("ball"+str(i),fill=color)
            canva.update()
            canva.after(50)

def start():
    step = random.randint(1,20)
    for ball in balls:
        canva.move(ball,step,0)
        if canva.coords(ball)[2]>=500:
            winner_color = canva.itemcget(ball, 'fill')
            messagebox.showinfo('Победа',f'Победил шар {winner_color}')
            return
    canva.after(50,start)

def balls_func():
    balls = [
        canva.create_oval(350, 250, 380, 280, fill="red"),
        canva.create_oval(350, 350, 380, 380, fill="green"),
        canva.create_oval(350, 450, 380, 480, fill="blue"),
        canva.create_oval(350, 550, 380, 580, fill="#fff")
    ]
    return  balls
def restart():
    return balls_func()

canva = Canvas(width=500,height=700)
canva.pack()

random_color=["red","blue","green"]

for i in range(16):
    color = random.choice(random_color)
    canva.create_oval(20+i*30,50,40+i*30,70,fill=color,tags="ball"+str(i))

canva.create_line(0,50,500,50)
canva.create_text(250,150,text='Нажми, для начала праздника',tags='start')
canva.tag_bind('start','<Button-1>',click)

balls = balls_func()

btn_start = Button(text="start",font="Arial 15",command=start)
btn_start.place(x=400,y=200)

btn_re_start = Button(text="restart",font="Arial 15",command=restart)
btn_re_start.place(x=200,y=200)

tk.mainloop()