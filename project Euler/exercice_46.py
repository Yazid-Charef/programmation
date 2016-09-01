import euler

a=list()
b=list()
d=list()
c=euler.premiers_sous(100000)
x=False
y=0
r=0
t=0

for i in range(1,6000,2):
    a.append(i)

    
for e in a:
    if(euler.test_premier(e)==False):
        b.append(e)


while(x==False):
    for i in b:
        for e in c:
            for u in range(1,100):
                if(i==e+2*u**2):
                    d.append(i)
                    break


for i in b:
    r=r+i
    print(r)
    
for i in d:
    y=y+i
    print(y)

print(r-y)
    
