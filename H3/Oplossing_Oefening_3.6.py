#Oefening 3.6
jaar = int(input("Welk jaar kwam de film uit?"))
rating = int(input("Geef een rating van 1-5:"))
basisprijs =  5
leeftijd_film = 2018 - jaar

if leeftijd_film > 2:
    basisprijs = basisprijs + 1
elif rating == 3 or 2:
    basisprijs = basisprijs + 1
elif rating == 4 or 5:
    basisprijs = basisprijs + 2

print(basisprijs)