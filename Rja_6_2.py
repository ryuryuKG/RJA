import glob
import json
import tkinter as tk
keypointinf = lambda pnum, json, kpn, data: json["people"][pnum]["pose_keypoints_2d"][kpn * 3 + data]

root = tk.Tk()
root.geometry("1920x1080")
canvas = tk.Canvas(root, background="#fff", width=1920, height=1080)
canvas.pack()
shlR_p1 = []
shlR_p2 = []
shlL_p1 = []
shlL_p2 = []
txt = glob.glob('kabeposter/kabeposter_000000000000_keypoints.json')
for file in txt:
    with open(file, 'r') as f:
        l = json.loads(f.read())
        shlR_p1 = [keypointinf(0, l, 2, i) for i in range(3)]
        shlL_p1 = [keypointinf(0, l, 5, i) for i in range(3)]
        shlR_p2 = [keypointinf(1, l, 2, i) for i in range(3)]
        shlL_p2 = [keypointinf(1, l, 5, i) for i in range(3)]

canvas.create_line(shlR_p1[0], shlR_p1[1], shlL_p1[0], shlL_p1[1], width=1)
canvas.create_line(shlR_p2[0], shlR_p2[1], shlL_p2[0], shlL_p2[1], width=1)
root.mainloop()
