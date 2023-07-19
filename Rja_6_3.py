import glob
import json
import tkinter as tk
import time

keypointinf = lambda pnum, json, kpn, data: json["people"][pnum]["pose_keypoints_2d"][kpn * 3 + data]

root = tk.Tk()
root.geometry("1920x1080")
canvas = tk.Canvas(root, background="#fff", width=1920, height=1080)
canvas.pack()

p1l=[]
p2l=[]

bodydict = {0:1,1:2,2:3,3:4,4:4,5:1,6:5,7:6,8:1,9:8,10:9,
            11:10,12:8,13:12,14:13,15:0,16:0,17:15,18:16,
            19:14,20:19,21:14,22:11,23:22,24:11,}
for txt in glob.glob('kabeposter/kabeposter_*_keypoints.json'):
    with open(txt, 'r') as f:
        l = json.loads(f.read())
        for j in range(25):
            p1l.append([keypointinf(0, l, j, i) for i in range(3)])
            p2l.append([keypointinf(1, l, j, i) for i in range(3)])
        for num in range(25):
            pair = int(bodydict[num])
            if p1l[num][2] != 0 and p1l[pair][2] != 0:
                canvas.create_line(p1l[num][0], p1l[num][1], p1l[pair][0], p1l[pair][1], width=1,tags="line")
            if p2l[num][2] != 0 and p2l[pair][2] != 0:
                canvas.create_line(p2l[num][0], p2l[num][1], p2l[pair][0], p2l[pair][1], width=1,tags="line")
    time.sleep(0.02)
    root.update()
    p1l.clear()
    p2l.clear()
    canvas.delete("line")
root.mainloop()