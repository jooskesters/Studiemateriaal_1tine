artikelnummer = int(input("Geef het artikelnummer van het product:"))
eenheidsprijs = 0
kassaticket = ""
totaal_bedrag = 0
while artikelnummer != 999:
    hoeveelheid = int(input("Geef de hoeveelheid producten:"))
    eenheidsprijs = float(input("Geef de eenheidsprijs van het product:"))
    artikelprijs = hoeveelheid * eenheidsprijs
    kassaticket += str(artikelnummer) + " " + str(hoeveelheid) + " "
    kassaticket += str(eenheidsprijs) + " " + str(artikelprijs) + "\n"
    totaal_bedrag += artikelprijs
    artikelnummer = int(input("Geef het artikelnummer van het product:"))
print("Artikelnummer is niet beschikbaar")
print(totaal_bedrag)
print(kassaticket)