sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for klic in sales:
    print(sales[klic])

for klic, hodnota in sales.items():
    print(f"nazev: {klic}, pocet prodanych kusu: {hodnota}")


hodnoceni = ["Kniha 1", 4, "Kniha 2", 5, "Kniha 3", 3.3]
hodnoceni1 = [
    ["Kniha1", 4], 
    ["Kniha2", 5], 
    ["Kniha3", 3.3]
]

print(hodnoceni1[0][1])
print(hodnoceni1[0][0][0])

for polozka in hodnoceni1:
    print(polozka[0] + " " + str(polozka[1]))



