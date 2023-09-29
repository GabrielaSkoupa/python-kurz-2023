jmeno = "gabriela.skoupa"
mail = jmeno + "@czechitas.cz"
print (mail)

krestni = input("Napiště prosím své křestní jméno bez diakritiky: ")
prijmeni = (input("Napiště prosím své příjmení bez diakritiky: "))
jmeno_a_prijmeni = krestni +  " " + prijmeni
print (jmeno_a_prijmeni.upper())
print (jmeno_a_prijmeni.lower())
print (krestni[0].upper() + krestni[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())