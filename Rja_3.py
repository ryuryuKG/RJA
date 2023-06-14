import glob
l=[]
for txt in glob.glob('sample/kitamura_****[1,3,5,7,9]_kgu.txt'):
    with open(txt) as f:
        l.append(int(f.read()))
print(sum(l))