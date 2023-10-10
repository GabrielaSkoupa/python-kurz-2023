sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

poptavana_soucastka = input("napište kód součástky, kterou si zákazník přeje: ")

#je součástka na skladě?
if poptavana_soucastka in sklad:
   poptavane_mnozstvi = int(input("Napište, kolik kusů si zákazník přeje: "))
   if poptavane_mnozstvi <= sklad[poptavana_soucastka]:
      
      #Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.
      sklad[poptavana_soucastka] = sklad[poptavana_soucastka]- poptavane_mnozstvi
      print(f"Součástek je dostatek, po prodeji bude zbývat: {sklad[poptavana_soucastka]} ks.")
   else:
      print(f"Lze prodat pouze {sklad[poptavana_soucastka]} kusů")
# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
else:
    print("Tato položka bohužel není skladem")

print(sklad)