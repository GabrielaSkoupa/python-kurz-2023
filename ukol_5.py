"""Mějme zadaný následující seznam naměřených teplot.
 Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci."""
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
"""Vytvoř seznam průměrných teplot pro každý den.
Vytvoř seznam ranních teplot.
Vytvoř seznam nočních teplot.
Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu."""

#1
prumerne_teploty=[sum(den)/len(den) for den in teploty]
print(f"průměrné teploty: {prumerne_teploty}")

#2
ranni_teploty=[den[0] for den in teploty]
print(f"ranní teploty: {ranni_teploty}")

#3
nocni_teploty=[den[-1] for den in teploty]
print(f"noční teploty: {nocni_teploty}")

#4
poledni_nocni=[[den[1],den[-1]] for den in teploty]
print(f"polední a noční teploty: {poledni_nocni}")