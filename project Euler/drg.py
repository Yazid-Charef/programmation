import euler

def test_pandigital(x):
    c=list()
    for e in str(x):
        for i in range(1,8):
            i=5
        if(i!=e):
            return False
    return True
                


if(test_pandigital(7652483)==False):
    print("yes")
