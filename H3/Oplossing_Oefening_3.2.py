#Oefening 3.2
brutoloon = float(input("Geef hier uw brutoloon:"))
jaarlijks_vakantiegeld = brutoloon * 0.05

if jaarlijks_vakantiegeld >= 350:
 jaarlijks_bijdrage= 350 * 0.08
else: jaarlijks_bijdrage = jaarlijks_vakantiegeld * 0.08

print(brutoloon)
print(jaarlijks_vakantiegeld)
print(jaarlijks_bijdrage)
