a=1
r=str()
while(len(str(r))<1000000):
    r=r+str(a)
    a=a+1
d=int(r[1-1])*int(r[10-1])*int(r[100-1])*int(r[1000-1])*int(r[10000-1])*int(r[100000-1])*int(r[1000000-1])
print(d)
    
