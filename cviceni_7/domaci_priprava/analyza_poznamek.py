celkem_radku = 0
neprazdne_radky = 0
pocet_znaku = 0
with open("poznamky.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        celkem_radku += 1
        cisty_radek = line.strip()
        if cisty_radek:
            neprazdne_radky += 1
            print (neprazdne_radky, cisty_radek)
        radek_bez_konce = line.rstrip("\r\n")
        pocet_znaku += len(radek_bez_konce)

print("Celkovy pocet radku:",celkem_radku )
print("Pocet neprazdnych radku:", neprazdne_radky)
print("Pocet znaku:", pocet_znaku)