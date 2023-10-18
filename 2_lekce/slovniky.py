knihy = ["Temna noc", 450, True, True]
knihy[0] = "Milosrdna vrazda"

knihy2 = {
    "Nazev": "Ananas na pizzu patri",
    "Cena": 0,
    "Skladem": True
}

print(knihy2)
print(knihy2.keys())
print(knihy2.values())
print(knihy2["Nazev"])
print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")

knihy2["Cena"] = 100

print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")

knihy2["Autor"] = "Michal Kucera"

print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")

if "autor" in knihy2:
    print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")
else:
    print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")