#Oefening 2.7
lengte= float(input("Geef de lengte van het tapijt (in meter):"))
breedte = float(input("Geef de breedte van het tapijt (in meter):"))
prijs_per_vierkante_meter = float(input("Geef de prijs per vierkante meter:"))
plaatsingskosten_per_vierkante_meter = (float(input("Geef de plaatsingskosten per vierkante meter:")))
kostprijs = prijs_per_vierkante_meter * lengte * breedte
totaal_plaatsingskosten = plaatsingskosten_per_vierkante_meter * lengte * breedte
totale_kosten = (kostprijs + totaal_plaatsingskosten)
print(kostprijs)
print(totaal_plaatsingskosten)
print(totale_kosten)

