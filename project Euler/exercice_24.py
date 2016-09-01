a=0
k=0
c=list()
d=list()
h=str()

b=[0,1,2]
c.append(b)
b.reverse()
c.append(b)


while(k<2):
	a=b[0]
	b[0]=b[2]
	b[2]=a
	c.append(intb)
	b.reverse()
	c.append(b)
	k=k+1
print(c)

for i in c:
    h=str(i)
    h=h.replace('[','')
    h=h.replace(']','')
    h=h.replace(',','')
    h=h.replace(' ','')
    d.append(h)
print(d)


