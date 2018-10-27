tekst = "ph@t 100t"
result = ""
for letter in tekst:
    if letter >= 'a' and letter <= "z":
        result += letter
    else:
        result += " "
print(result)