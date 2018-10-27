n = int(input("Geef hier het aantal karakters dat u nodig hebt"))
som = 0
while n != 0:
    n -= 1
    inp = input("Geef hier een karakter in")
    if inp >= "0" and inp <= "9":
        som += int(inp)
    elif inp == inp.upper():
        print(inp, "Is een hoofdletter")
    elif inp == inp.lower():
        print(inp, "is een kleine letter")
    else:
        print(inp, "Is een onbekend karakter")
print(som)
print("je karakters zijn op")
