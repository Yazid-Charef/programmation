c=0
e=list()
for a in range(100,999):
    for b in range(100,999):
        c=a*b
        if (str(c) == str(c)[::-1]):
            e.append(c)
            
            
print(max(e))           
    
