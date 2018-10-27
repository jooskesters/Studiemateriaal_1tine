from random import randint
getallen = []
groter_dan = 0
totaal = 0
for i in range(500):
    getal = randint(0,10000)
    getallen.append(getal)
    if getal > 5000:
        groter_dan += 1


grens = 8000
if groter_dan < 250:
    grens = 5000

print(grens)
for getal in getallen:
    if getal > grens:
        totaal += getal

print(totaal)