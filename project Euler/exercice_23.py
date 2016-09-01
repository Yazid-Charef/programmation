import euler

x=1
r=0
a=0
c=list()
d=list()
f=0

while(x<28123):
    r=0
    a=euler.diviseur(x)
    for i in a:
        r=r+i
    if(r<x):
        c.append(x)
    x=x+1
    
for i in c:
    for o in c:
        if (o>i):
            f=f+i+o
            d.append(f)
print(f)
        
