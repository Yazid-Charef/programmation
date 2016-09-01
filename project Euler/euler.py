def diviseur(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors


def test_premier(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def test_palindrome(nb):
    if str(nb) == str(nb)[::-1]:
        return True
    return False

def premiers_sous(end):
    if end < 2:
        return []
    lng = (end//2) - 1
    primes = [True]*lng  
    for i in range(int(lng**0.5)):  
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False  
    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

def test_abundant(n):
    return sum(divisors(n))+1 > n

def fibonacci(n) :
    a,b,c=1,1,1
    if (n==1) :
        print(a)
    elif (n==2) :
        print(b)
    else :
        while (c<n-2) :
            a,b,c=b,a+b,c+1
        print(a+b)
