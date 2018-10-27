som = 0
AANTAL_STUDENTEN = 10
for i in range(1, AANTAL_STUDENTEN + 1):
    leeftijd = int(input("Student" + str(i) + ": geef je leeftijd: "))
    som += leeftijd
print("Gemiddelde leeftijd: ", som / AANTAL_STUDENTEN)
