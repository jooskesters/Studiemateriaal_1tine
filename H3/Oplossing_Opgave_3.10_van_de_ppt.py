gewicht = float(input("Geef het gewicht van de koffer:"))
if gewicht > 20:
    print("Er moet een toeslag van 25 euj betaald worden voor bagage die te zwaar is.")
elif gewicht < 20:
    print("Goede reis!")
else:
    print("Poeh! Dat gewicht is precies goed!")