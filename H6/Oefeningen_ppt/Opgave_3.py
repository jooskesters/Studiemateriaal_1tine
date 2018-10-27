s1 = "lepel"
s2 = "rebel"

lengte = len(s1)
if len(s2) < lengte:
    lengte = len(s2)

for i in range(lengte):
    if s1[i] == s2[i]:
        print("index:", i, "karakter:", s1[i])
