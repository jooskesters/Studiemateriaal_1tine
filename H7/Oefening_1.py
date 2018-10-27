getallen = []
getal = 0
totaal = 0
kleiner_gemiddelde = 0
for i in range(15):
    getal = int(input("Geef hier een getal in: "))
    totaal += getal
    getallen.append(getal)
gemiddelde = totaal / len(getallen)
for i in range(15):
    if getallen[i] < gemiddelde:
        kleiner_gemiddelde += 1
print("Het gemiddelde is {:.1f}".format(gemiddelde))
print(kleiner_gemiddelde/15*100)