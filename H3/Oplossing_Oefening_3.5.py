#Oefening 3.5
hoeveelheid_artikels = int(input("Hoeveel artikels wenst u?"))
eenheidsprijs_artikel = 11.50
BTW_PERCENTAGE = 1.21
totaal_prijs = hoeveelheid_artikels * eenheidsprijs_artikel * BTW_PERCENTAGE
korting = totaal_prijs * 0.10

if totaal_prijs > 1000:
    print(("De totale prijs bedraagt"), totaal_prijs - korting)
else:
    print(totaal_prijs)
