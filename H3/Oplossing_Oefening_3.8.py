#Oefening 3.8
afstand_vlucht_in_km = float(input("Geef het aantal kilometers van de vlucht (in km):"))
toeristenklasse = 1
charset = 2
zakenreis = 3
klasse = int(input("in welke klasse vloog u:"))

if afstand_vlucht_in_km < 1000:
    prijs = 0.25 * afstand_vlucht_in_km
elif afstand_vlucht_in_km > 1000 and afstand_vlucht_in_km < 3000:
    prijs = 0.20 * afstand_vlucht_in_km
else:
    prijs = 0.12 * afstand_vlucht_in_km

if klasse == 1:
    print(prijs)
elif klasse == 2:
    print(prijs - prijs*0.20)
else:
    print(prijs *1.30)





