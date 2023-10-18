def hello_world():
    print("Hello world")

def hello_user(name):
    print("Hello, " + name)

def get_name():
    name = input("Name:")
    return name

def pizzeria(nazev, ananas = True):
    return f"Objednal sis pizzu {nazev}, obsahuje ananas: {ananas}"

def zpracuj_prihlasku(jmeno, gender=""):
    return f"{jmeno}, {gender}"

def znamky(seznam):
    novy_seznam = []
    # [vyborny, chvalitebny, dobry, dobry...]

    for znamka in seznam:
        if znamka == 1:
            novy_seznam.append("vyborny")
        elif znamka == 2:
            novy_seznam.append("chvalitebny")
        elif znamka == 3:
            novy_seznam.append("dobry")
        elif znamka == 4:
            novy_seznam.append("dostatecny")
        elif znamka == 5:
            novy_seznam.append("nedostatecny")
        else:
            novy_seznam.append("ERROR")

    return novy_seznam

hodnoceni = [1, 2, 3, 3, 2, 1, 5]
print(znamky(hodnoceni))
print(znamky([1, 3, 5, 6, 3, 1, -1]))
nezaokrouhlene_cislo = 3.5
print(round(nezaokrouhlene_cislo))

print(pizzeria("Hawaii", False))
print(pizzeria("Salami"))

jmeno = input("Zadej jmeno: ")
gender = input("Zadej gender: ")

if gender == "":
    print(zpracuj_prihlasku(jmeno))
else:
    print(zpracuj_prihlasku(jmeno, gender))

React

Reply










