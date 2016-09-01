import euler

x=list()
r=0

for a in range(0,1000000):
    if(euler.test_palindrome(a)):
        b=bin(a)[2:]
        if(euler.test_palindrome(b)):
            x.append(a)
            
        
for i in x:
    r=r+i

    
print(r)
