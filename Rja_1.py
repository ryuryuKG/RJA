import re

sum=0
with open('C:\大学\研究室\領域実習\RJA\data.txt') as f:
    lines = f.read()
    for l in lines.split("\n"):
        if re.fullmatch(r"-?\d+",l):
            sum=sum+int(l)
print(sum)

