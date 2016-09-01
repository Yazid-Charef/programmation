import euler


x=600851475143
n= euler.diviseur(x)
n.sort(reverse=True)



for a in n:
    if(euler.test_premier(a)):
        print(a)
        break

