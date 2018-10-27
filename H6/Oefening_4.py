woord_een = input("Geef hier een woord:")
woord_twee = input("Geef hier nog een woord:")

while len(woord_een) < 4:
    woord_een += "*"

while len(woord_twee) < 4:
    woord_twee = "+" + woord_twee

woord_3 = woord_een[0:4].upper() + woord_twee[-4:]
print(woord_3)
