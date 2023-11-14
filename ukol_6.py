class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
    
    def pujc_auto (self):
        if self.dostupne == True:
            self.dostupne == False #Tady někde bude chyba, nevím, jak to změnit na false
            print("Potvrzuji zapůjčení vozidla")
        else: 
            print("Vozidlo není k dispozici")
        
    def get_info (self):
        print (f"vozidlo se značkou {self.registracni_znacka}, typ {self.typ_vozidla}")


Auto_1 = Auto ("4A2 3020", "Peugeot 403 Cabrio", 47534)
Auto_2 = Auto ("1P3 4747", "Škoda Octavia", 41253 )

pujcka = input("jaké auto si přejete půjčit? Peugeot nebo Škoda?") 
if pujcka == "Peugeot":
   Auto_1.get_info()
   Auto_1.pujc_auto()   
elif pujcka == "Škoda":
    Auto_2.get_info()
    Auto_2.pujc_auto()
else: print("Toto auto nevlastníme")

