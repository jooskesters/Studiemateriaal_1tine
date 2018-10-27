tekst = "Dt was eEn tEkst"
index_of_t = tekst.upper().find("T")
nieuwe_tekst = tekst[0:index_of_t + 1]
if index_of_t == -1:
    print("De gegeven tekst bevat geen t of T.")

if len(tekst) % 2 == 0:
    nieuwe_tekst = nieuwe_tekst + tekst[index_of_t + 1:].lower()
    print(nieuwe_tekst)

else:
    nieuwe_tekst = nieuwe_tekst + tekst[index_of_t + 1:].upper()
    print(nieuwe_tekst)
