stri = str(input("Geef hier een tekst in: "))
l1 = list(stri)
empty_l = []
for i in range(0, len(l1)):
    a = 0
    if i not in empty_l:
        for j in range(0, len(l1)):
            if l1[i] == l1[j]:
                a = a + 1
                empty_l.append(j)
                print(l1[j],a)