hoogte = int(input("Geef de hoogte van de driehoek:"))
for i in range(hoogte):
    for k in range(hoogte - i):
        print("@", end = " ")
    print("\n")