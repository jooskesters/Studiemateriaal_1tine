#Oefening 3.9
A = int(input("Geef een geheel getal:"))
B = int(input("Geef nog een geheel getal:"))
c = int(input("Geef de gewenste bewerking (code 1 t.e.m 5):"))
if c == 1:
    optelling = (A + B)
elif c == 2:
    aftrekking = (A - B)
elif c == 3:
    vermenigvuldiging = (A * B)
elif c == 4:
    kwadraat_A = (A ** 2)
elif c == 5:
    kwadraat_B = (B ** 2)
else:
    print("foutieve code")