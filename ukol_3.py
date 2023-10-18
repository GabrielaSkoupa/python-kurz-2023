"""Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json."""
import json
with open("body.json", mode="r", encoding="utf-8") as file:
    ukol_body=json.load(file)

print(ukol_body.items())

pass_fail = {}
for student, body in ukol_body.items():
    if body>= 60:
       pass_fail[student]="Pass"
    else:
        pass_fail[student]="Fail"

print(pass_fail)

import json
pass_fail 
with open("prospech.json", mode="w", encoding="utf-8") as output_file: json.dump(pass_fail, output_file)

#nepřišla jsem na to, jak nebo kam napsat to ensure_ascii=False, aby mi to psalo znaky s diakritikou, tak aspoň takto