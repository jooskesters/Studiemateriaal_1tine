inschrijvingsnummer = int(input("Geef inschrijvingsnummer:"))
snelste_renner = 0
snelste_tijd = 0
aantal_renners_boven_uur = 0
aantal_renners = 0
while inschrijvingsnummer >= 0:
    aantal_renners += 1
    tijd = int(input("Geef tijd in sec.:"))
    if snelste_tijd == 0 or tijd < snelste_tijd:
        snelste_tijd = tijd
        snelste_renner = inschrijvingsnummer
    if tijd < 3600:
        aantal_renners_boven_uur += 1
    inschrijvingsnummer = int(input("Geef inschrijvingsnummer"))
print("Snelste renner:", snelste_renner)
print("Snelste tijd:", snelste_tijd)
print("Totaal aantal renners:", aantal_renners)
print("Percentage boven uur:", aantal_renners_boven_uur / aantal_renners * 100, "%")