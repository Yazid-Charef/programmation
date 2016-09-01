import euler

def nb_triangulaire(x):
    a=0
    for i in range(0,x+1):
        a=a+i
    return a


def nb_diviseur(x):
    g=0    
    r=0
    g=euler.diviseur(x)
    for i in g:
        r=r+1
    return r    
        
   
y=1


while(nb_diviseur(nb_triangulaire(y))<500):
    y=y+1
print(nb_triangulaire(y))
print(nb_diviseur(nb_triangulaire(y)))
    
