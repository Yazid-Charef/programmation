from string import ascii_lowercase as alphabet

p=open("exercice_42_nombres.txt","r")
a=p.read()
p.close()
a=a.replace(' ','')
b=list()
r=int()
y=int()
for i in a:
    for e in i:
        r=alphabet.find(e)
        y=y+r
    b.append(y)
    y=0
print(b)
