import json

with open("pizza.json", mode="r", encoding="utf-8") as soubor:
    pizzy = json.load(soubor)

print(pizzy["ingredience"][-1])
print(pizzy["ingredience"][3])