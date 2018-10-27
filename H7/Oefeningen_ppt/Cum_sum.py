def cum_sum(mijn_lijst):
    for i in range(1, len(mijn_lijst)):
        mijn_lijst[i] = mijn_lijst[i - 1] + mijn_lijst[i]


lijst = [7, 8, 13, 8, 5, 2, 8]
cum_sum(lijst)
print(lijst)
