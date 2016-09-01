import euler


def test_pandigital(x):
    y=str(x)
    e=0
    for i in range(1,8):
        if(y.count(str(i))>1):
            e=1
            break
        elif(y.count(str(i))==0):
            e=1
            break
    if(e==0):
        return True
    else:
        return False

                




x=7654321
while not(test_pandigital(x) and euler.test_premier(x)):
        x=x-2

    
print(x)
