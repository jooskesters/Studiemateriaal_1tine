def zoek_voorkomens(mijn_lijst, waarde):
    indexen = []
    aantal = 0
    for i in range(len(mijn_lijst)): # range(7) -> 0 1 2 3 4 5 6
        if mijn_lijst[i] == waarde:
            aantal += 1
            indexen.append(i)
    print(waarde, "komt ", aantal, "keer voor")
    print("op index ", indexen)
lijst = [7,8, 13, 8, 5, 2, 8]
zoek_voorkomens(lijst, 8)