import glob
sum=0
for txt in glob.glob('sample/kitamura_****[1,3,5,7,9]_kgu.txt'):
    with open(txt) as f:
        sum=sum+int(f.read())
print(sum)