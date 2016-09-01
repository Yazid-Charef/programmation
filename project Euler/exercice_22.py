p=open("exercice_22_nom.txt","r")
a=list(eval(p.read()))
p.close()
r=int()

x=list()
c=str()
h=list()
g=int()

a.sort()



for i in a:
    r=0
    for e in i:
        r=r+(ord(e)- 64)
    r=r*(a.index(i)+1)
    h.append(r)

for i in h:
    g=g+i
print(g)
