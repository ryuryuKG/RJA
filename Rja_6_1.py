import glob
import json
import re

def Keypointinf(pnum,json,kpn):
        pl=[]
        pl.append(json["people"][pnum]["pose_keypoints_2d"][kpn*3])
        pl.append(json["people"][pnum]["pose_keypoints_2d"][kpn*3+1])
        pl.append(json["people"][pnum]["pose_keypoints_2d"][kpn*3+2])
        return pl


keypointnumber=0

h_p1=[]
h_p2=[]
n_p1=[]
n_p2=[]
txt = glob.glob('kabeposter/kabeposter_000000000000_keypoints.json')
for file in txt:
    with open(file, 'r') as f:
        l= json.loads(f.read())
        h_p1=Keypointinf(0,l,0)
        h_p2=Keypointinf(1,l,0)
        n_p1=Keypointinf(0,l,1)
        n_p2=Keypointinf(1,l,1)
print("1人目鼻",h_p1)
print("1人目首",n_p1)
print("2人目鼻",h_p2)
print("2人目首",n_p2)





