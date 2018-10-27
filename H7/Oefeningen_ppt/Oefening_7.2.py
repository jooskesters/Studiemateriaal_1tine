getallenlist = [17, 24, 8, 14, 32, 30]
hoogste = getallenlist[0]
for i in range(1, len(getallenlist)):
    if getallenlist[i] > hoogste:
        hoogste = getallenlist[i]
print("Het grootste getal= ", hoogste)


getallenlist = [17, 24, 8, 14, 32, 30]
laagste = getallenlist[0]
for i in range(1, len(getallenlist)):
    if getallenlist[i] < laagste:
        laagste = getallenlist[i]
print("Het laagste getal= ", laagste)

getallenlist = [17, 24, 8, 14, 32, 30]
som = 0
for i in range(0, len(getallenlist)):
    som += getallenlist[i]

