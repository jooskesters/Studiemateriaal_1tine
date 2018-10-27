#Opgave lidgeld
ONGEHUWD = 1
GEHUWD = 2
WEDUWNAAR = 3
burgerlijke_staat = int(input("Geef uw burgerlijke staat: 1 = ongehuwd; 2 = gehuwd; 3 = weduwnaar"))
leeftijd = int(input("Geef uw leeftijd:"))

#ongehuwd: 25 euro; gehuwd: 20 euro; weduwenaar: 15 euro.
lidgeld_A = 25
if burgerlijke_staat == GEHUWD:
    lidgeld_A = 20
elif burgerlijke_staat == WEDUWNAAR:
    lidgeld_A = 15
print("A)", lidgeld_A)

#ongehuwd jonger dan 30: 25 euro; alle overige betalen 15 euro.
lidgeld_B = 15
if burgerlijke_staat == ONGEHUWD and leeftijd < 30:
    lidgeld_B = 25
print("B) ", lidgeld_B)

#alle leden jogner dan 30 en alle ongehuwden: 25 euro; alle overige betalen 15 euro.
lidgeld_C = 15
if burgerlijke_staat == ONGEHUWD or leeftijd < 30:
    lidgeld_C = 25
print("C) ", lidgeld_C)

#ongehuwd 25 euro; gehuwd jonger dan 30: 20 euro; alle overige betalen 15 euro.
lidgeld_D = 25
if burgerlijke_staat == GEHUWD and leeftijd < 30:
    lidgeld_D = 20
elif burgerlijke_staat == ONGEHUWD:
    lidgeld_D = 25
else:
    lidgeld_D = 15
