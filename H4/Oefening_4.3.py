num = 1
totaal = 0
teller = 0
negative = 0
while num != 0:
    num = int(input("Geef een nummer in: "))
    totaal += num
    if num < 0:
        negative += 1
print(totaal)
print(negative)



