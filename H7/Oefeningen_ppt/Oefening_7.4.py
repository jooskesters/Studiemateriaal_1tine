lijst = []
som = 0
for i in range(1, 10):
    gegeven_getal = int(input("Geef een getal: "))
    lijst.append(gegeven_getal)
    som += gegeven_getal
print(lijst)
gemiddelde = som / len(lijst)
print("Het gemiddelde is: ", gemiddelde)
klein_lijst = []
for getal in lijst:
    if getal < gemiddelde:
        klein_lijst.append(getal)
print("Alle getallen die kleiner zijn dan het gemiddelde zijn: ")
print(klein_lijst)
print("Het aantal kleine getallen is: ", len(klein_lijst))
