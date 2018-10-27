hoogte = int(input("Geef de hoogte van de driehoek: "))
char = input("Geef het start-karakter: ").upper()
for i in range(hoogte):
    for j in range(i + 1):
        print(char, end=" ")
        char = chr(ord(char) + 1)
        if char > "Z":
            char= "A"
    print()