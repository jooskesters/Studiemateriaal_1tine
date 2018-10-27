def druk_lijn(i,grootte):
    for j in range(i):
        print(" ", end= " ")
    for j in range (grootte - i):
        print("*", end="")


grootte = 5
for i in range(grootte):
    druk_lijn(i, grootte)
    print()