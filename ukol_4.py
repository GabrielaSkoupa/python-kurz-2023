"""První funkce ověří telefonní číslo.
 Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). 
Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False."""

def format_cisla():
    cislo = input("zadejte telefonní číslo příjemce: ")
    if len(cislo):9
    delka_cisla = True

    elif len(cislo):13 
    delka13 = True
    elif cislo[:3]:"+420"
    predvolba = True
        if delka13 and predvolba:
        delka_cisla = True
    else:
        delka_cisla = False 
    print(delka_cisla)


    
format_cisla()

