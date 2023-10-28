def format_cisla():
    cislo = input("zadejte telefonní číslo příjemce: ")
    delka_cisla = True
    if len(cislo)==9:
        delka_cisla = True
    elif len(cislo)==13 and cislo[:4]=="+420":
        delka_cisla = True
    else:
        delka_cisla = False 
    print("neprávný formát čísla")

    return delka_cisla

def cena_zpravy():
    if delka_cisla == True:
        text = input("zadejte text zprávy: ")

    if len(text)<=180:
        print ("Cena vaší zprávy je 3 Kč.")
    elif len(text)>=181 and len(text)<= 360:
        print("Cena vaší zprávy je 6 Kč.")
    elif len(text)>=361 and len(text)<= 540:
        print("Cena vaší zprávy je 9 Kč.")
    else:
        print("vaše zpráva je moc dlouhá")

format_cisla() 
if delka_cisla == True:
    cena_zpravy()

