a=int(input())
e=int(input())
d=int()

ta=a*a
te=e*e


if(ta>te):
   d=ta-te
   if(d>10):
      print("La famille Arignon a un champ trop grand")
elif(ta<te):
   d=te-ta
   if(d>10):
      print("La famille Evaran a un champ trop grand")
