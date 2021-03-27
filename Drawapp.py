name=input("Nume: ")
import random
viata=100
power=random.randrange(1,100)
inam= 150
m=random.randrange(1,20)

print("Ce vrei sa faci?")
print("Lobveste - 1")
print("Adauga viata - 2")
ch=int(input("Varianta: "))
if (ch ==1):
    print(name,"-",m)
    if(viata == 0):
        print("Offf")
    else:
        print("Bot turn")
        viata=viata-m
        if viata == 90:
             print("Ai viata egala cu  90 ",viata)
        if viata <= 60 and viata<=40:
             print("Ai viata <  60 ",viata)
        if viata <= 40:
             print("Ai viata ",viata)
        if(viata != 0):
             print(viata,"viata")
        print("your turn")
        power=random.randrange(1,100)
        inam=inam-power
        print("-",inam)
else:
     if (ch ==2):
          print("Viata",viata,"+","20")
          vr=viata+20
          if (vr>100):
               print("Ai viata 100!")
               viata=vr-100+viata
               viata=viata+20



if(inam == 0):
     print("Yay")
print("Ce vrei sa faci?")
print("Lobveste - 1")
print("Adauga viata - 2")
ch=int(input("Varianta: "))
if (ch ==1):
    print(name,"-",m)
    if(viata == 0):
        print("Offf")
    else:
        print("Bot turn")
        viata=viata-m
        if viata == 90:
             print("Ai viata egala cu  90 ",viata)
        if viata <= 60 and viata<=40:
             print("Ai viata <  60 ",viata)
        if viata <= 40:
             print("Ai viata ",viata)
        if(viata != 0):
             print(viata,"viata")
        print("your turn")
        power=random.randrange(1,100)
        inam=inam-power
        print("-",inam)
else:
     if (ch ==2):
          print("Viata",viata,"+","20")
          vr=viata+20
          if (vr>100):
               print("Ai viata 100!")
               viata=vr-100+viata
               viata=viata+20



if(inam == 0):
     print("Yay")
print("Ce vrei sa faci?")
print("Lobveste - 1")
print("Adauga viata - 2")
ch=int(input("Varianta: "))
if (ch ==1):
    print(name,"-",m)
    if(viata == 0):
        print("Offf")
    else:
        print("Bot turn")
        viata=viata-m
        if viata == 90:
             print("Ai viata egala cu  90 ",viata)
        if viata <= 60 and viata<=40:
             print("Ai viata <  60 ",viata)
        if viata <= 40:
             print("Ai viata ",viata)
        if(viata != 0):
             print(viata,"viata")
        print("your turn")
        power=random.randrange(1,100)
        inam=inam-power
        print("-",inam)
        print(viata)
else:
     if (ch ==2):
          print("Viata",viata,"+","20")
          vr=viata+20
          if (vr>100):
               print("Ai viata 100!")
               viata=vr-100+viata
               viata=viata+20



if(inam == 0):
     print("Yay")
          



