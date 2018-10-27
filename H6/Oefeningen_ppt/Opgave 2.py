tekst = "Going to the movies"

for i in range(len(tekst)):
    if tekst[i] in "aeiou": #is een klinker ?
        print("index:", i, "letter", tekst[i])
