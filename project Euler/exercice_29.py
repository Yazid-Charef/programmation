b=list()
c=list()
r=0

for a in range(2,101):
    for z in range(2,101):
        b.append(a**z)

b=list(set(b))
b.sort()

for i in b:
    r=r+1
print(r)


        
