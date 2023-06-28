import math
import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
canvas = tk.Canvas(root, background="#fff", width=500, height=500)
canvas.pack()
def create_bone(X0, Y0, range, angle):
    r = math.radians(angle)
    canvas.create_line(X0, Y0, range * math.sin(r) + X0, range * math.cos(r) + Y0, fill="Black", width=1, tag="body")
def move():
    canvas.move("body", 5, 0)
    canvas.after(100, move)
button = tk.Button(root, text="GO", command=move)
button.place(x=0,y=0)
X = 200
Y = 150
R = 60
create_bone(X, Y - R, 2 * R, 0)
create_bone(X, Y, R + 40, 120)
create_bone(X, Y, R + 40, 240)
create_bone(X, Y + R, R + 40, 30)
create_bone(X, Y + R, R + 40, 330)
canvas.create_oval(X - 25, Y - (50 + R), X + 25, Y - R, width=1, tag="body")
root.mainloop()