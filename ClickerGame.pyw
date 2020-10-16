from tkinter import *
from time import sleep
root=Tk()
root.title('Killable Process #1')
root.geometry('1920x1080')
root['bg'] = 'black'
global points
points=0
def AddPoint():
    global points, pointscount
    points +=1 
    pointscount=Label(text='Points: '+str(points))
    print(points)

def HideCheckPoint():
    global submit
    submit.pack_forget()
    pointscount.pack_forget()
    submit=Button(text='Check Points', command=CheckPoint)
    submit.pack()
def CheckPoint():
    global submit
    submit.pack_forget()
    pointscount.pack()
    submit=Button(text='Hide', command=HideCheckPoint)
    submit.pack()
# Check button has an issue where if you add a point before clicking hide something goes wrong. I'm just happy I finally got this working
jotaro=Button(text='Click for points', command=AddPoint)
jotaro.pack()
def SetBlack():
    root['bg'] = 'black'
    darkmode=Button(bg='white', text='Dark Mode', command=SetBlack)
    lightmode=Button(bg='white', text='Light Mode', command=SetWhite)
    darkmode.place(x=0, y=0)
    lightmode.place(x=100, y=0)
def SetWhite():
    root['bg'] = 'white'
    darkmode=Button(bg='black', fg='white', text='Dark Mode', command=SetBlack)
    lightmode=Button(bg='black', fg='white', text='Light Mode', command=SetWhite)
    darkmode.place(x=0, y=0)
    lightmode.place(x=100, y=0)
darkmode=Button(text='Dark Mode', command=SetBlack)
lightmode=Button(text='Light Mode', command=SetWhite)
submit=Button(text='Check Points', command=CheckPoint)
submit.pack()
def exit():
    root.destroy()
e=Button(text='Exit', command=exit)
e.place(x=1312, y=0)
darkmode.place(x=0, y=0)
lightmode.place(x=100, y=0)
pointscount=Label(text="Points: 0")
root.mainloop()