m=list()
r=int()
b=int()
c=int()
f=int()

while (f<6):
    r=0
    for i in str(b):
        r=r+int(i)**5
    if(r==b and b>2):
        m.append(b)
        f=f+1
    b=b+1 

        
for p in m:
    c=c+p
print(c)
