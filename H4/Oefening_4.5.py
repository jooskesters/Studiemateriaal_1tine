var1 = int(input("Geef een getal:"))
while var1 < 0 or var1 > 100:
    if var1 < 0:
        print("Het getal is te klein")
    elif var1 > 100:
        print("Het getal is te groot")
    var1 = int(input("Geef nog een getal:"))
print(var1)