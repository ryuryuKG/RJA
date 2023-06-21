import math
import tkinter as tk
def create_bone(X0,Y0,range,angle):
    r=math.radians(angle)
    canvas.create_line(X0,Y0,range*math.sin(r)+X0,range*math.cos(r)+Y0,fill="Black", width=1)

root = tk.Tk()
root.geometry("500x500")
canvas = tk.Canvas(root, background="#fff", width=500, height=500)
canvas.pack()
X=200
Y=150
R=60
create_bone(X,Y-R,2*R,0)
create_bone(X,Y,R+40,120)
create_bone(X,Y,R+40,240)
create_bone(X,Y+R,R+40,30)
create_bone(X,Y+R,R+40,330)
canvas.create_oval(X-25,Y-(50+R),X+25,Y-R, width=1)
# canvas.create_line(X, Y, X, Y+L, fill = "Black", width = 3)
root.mainloop()