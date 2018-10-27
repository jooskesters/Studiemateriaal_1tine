voornaam = input("Geef hier uw naam")
naam = input("Geef hier uw achternaam")

resultaat = voornaam[0].upper() + ". "
resultaat += naam[0].upper() +naam[1:].lower()
print(resultaat)
