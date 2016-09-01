x=1
y=0
t=list()
p=list()
h=list()
r=int()

while(y!=3):
    a=x*(x+1)/2
    t.append((x*(x+1))/2)
    p.append((x*(3*x-1))/2)
    h.append(x*(2*x-1))
    if(a in p):
        if(a in h):
            y=y+1
            r=x*(x+1)/2
            
    x=x+1

print(r)


