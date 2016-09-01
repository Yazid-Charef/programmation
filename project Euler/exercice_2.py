n = 2
a,b,c=1,1,1
x=2

if (n==2) :
    print(a*2)
    n=n+1


while (c<=n-2) :
     a,b,c=b,a+b,c+1
     if((a+b)%2==0 and a+b<4000000):       
       x=x+a+b
       print(x)
       n=n+1
       
     else:
       n=n+1
        

