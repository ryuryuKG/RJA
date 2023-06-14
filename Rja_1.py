import re
with open('data.txt') as f:
#     lines = f.read()
#     for l in lines.split("\n"):
#         if re.fullmatch(r"-?\d+",l):
#             sum=sum+int(l)
#print(sum)
    print(sum([int(l) for l in f.read().split("\n") if re.fullmatch(r"-?\d+",l)]))

