p=open("exercice_13_nombres.txt","r")
a=p.read()
p.close()
a=a.replace(' ','')
c=0
r=0
b=list()


for e in range(50,5001,50):
   c=a[e-50:e]
   b.append(c)

for n in b:
   r=r+int(n)
r=str(r)
print(r[:10])

