#Oplossing_Oefening_3.11
rating = int(input("Geef het aantal sterren (1-5):"))
formule = str(input("Geef de gekozen formule O(enkel ontbijt), H(half-pension), V(vol pension), A(all-inclusive):"))
aantal_overnachtingen = int(input("Geef het aantal dagen dat u verblijft:"))
seizoen = str(input("Geef de code van het seizoen in H(hoogseizoen), L(laagseizoen), T(tussenseizoen):"))
if rating == int(1):
    overnachtingskosten =  30 * aantal_overnachtingen
elif rating == int(2) or rating == int(3):
    overnachtingskosten = 40 * aantal_overnachtingen
else:
    overnachtingskosten = 55 * aantal_overnachtingen

print("Dit zijn de overnachtingskosten", overnachtingskosten)

ontbijt = 0
if formule == str("O"):
    ontbijt = overnachtingskosten * 0.20
elif formule == str("H"):
    ontbijt = overnachtingskosten * 0.50
elif formule == str("V"):
    ontbijt = overnachtingskosten * 0.60
elif formule != str("A"):
    print("ERROR betreffende de formule")
else:
    ontbijt = (overnachtingskosten * 0.60) + 80

totaalprijs = overnachtingskosten + ontbijt
print("Dit is de gekozen formule", formule)
print("Dit is het bedrag van het ontbijt gedurende het verblijf", ontbijt)


if seizoen == str("L"):
    if formule == str("O") or str("H"):
        totaalprijs = totaalprijs * 0.90
else:
    print("Er wordt geen extra korting toegekend")

print("Het totaal te betalen bedrag voor één persoon bedraagt",totaalprijs)
