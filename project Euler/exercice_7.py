import euler


y=1
x=0
z=list()
while(x!=10001):
    if(euler.test_premier(y)):
        z.append(y)
        x=x+1
        y=y+1
    else:
        y=y+1
print(max(z))        
    
    
