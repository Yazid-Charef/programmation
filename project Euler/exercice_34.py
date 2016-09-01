def fact(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x


x=3
a=list()
r=0
y=0
while(x<100000):
    r=0
    a=map(int, list(str(x)))
    for i in a:
        r=r+fact(i)
    if(r==x):
        y=y+x
    x=x+1
print(y)
