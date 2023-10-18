def mult (a, b):
    return a * b

print(mult (5,8))

#dělení
def divide(a,b):
    if b==0:
        print ("chyba")
        return
    else:
        return a/b    
    
print(divide(10, 2))


def kilometry_na_mile(kilometry):
    return kilometry * 1,609344

def mile_na_kilometry(mile):
    return mile / 1.609344

print(mile_na_kilometry(5))




