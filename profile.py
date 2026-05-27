import random

zahl = random.randint(1, 10)
versuche = 0
gewonnen = False
while versuche < 5:
    rate_zahl = int(input("rate die zahl "))
    versuche +=1
    if rate_zahl < zahl:
        print("zu niedrig")
    elif rate_zahl > zahl:
        print("zo hoch")
    else:
        print("richtig")
        gewonnen = True
        break
if gewonnen:
    (print("du hast gewonnen"))
else:
    print("du hast verloren. die gesuchte zahl war: ", zahl)