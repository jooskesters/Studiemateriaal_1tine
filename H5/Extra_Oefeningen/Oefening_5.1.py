def berekening(n):
    y = 0
    x = 1
    teller = 1
    while teller <= n:
            teller += 1
            y += (-1) ** teller*1/x
            x += 2
    return float(y * 4)


n = float(input("Geef hier het aantal stappen"))
print(berekening(n))
