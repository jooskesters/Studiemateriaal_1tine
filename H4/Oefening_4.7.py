temperatuur = int(input("Geef de temperatuur van vandaag:"))
grootste = 0
gemiddelde = 0
for i in range(10):
    if temperatuur > grootste:
        grootste = temperatuur
    gemiddelde += temperatuur
    temperatuur = int(input("Geef de temperatuur van vandaag:"))
print(grootste)
print(gemiddelde / 10)
