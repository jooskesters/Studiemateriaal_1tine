student1 = "An Janssen"
student2 = "Bart Vriends"
student3 = "Andries Michels"
student4 = "Inge Kaas"
code = 1
l1 = []
while code != 0:
    code = int(input("Geef hier een code in: "))
    if 0 < code < 5:
        l1.append(code)
print(len(l1))
print(sorted(l1))


percentage1 = l1.count(1) / 30 * 100
percentage2 = l1.count(2) / 30 * 100
percentage3 = l1.count(3) / 30 * 100
percentage4 = l1.count(4) / 30 * 100
percentage5 = l1.count(5) / 30 * 100
student1 += str(": ") , str(l1.count(1)), str(percentage1)
student2 += str(": "), str(l1.count(2)), str(percentage2)
student3 += str(": "), str(l1.count(3)), str(percentage3)
student4 += str(": "), str(l1.count(4)), str(percentage4)
print(student1)

