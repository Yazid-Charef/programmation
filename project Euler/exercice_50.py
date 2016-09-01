import euler
b=list()
q=0
u=3
for i in range(1, 100000):
    if (euler.test_premier(i)):
        b.append(i)


        
while(q<1000000):
        q=q+b[u]
        print(q)
        u=u+1
 
    
    
print(q)
