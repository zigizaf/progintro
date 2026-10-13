vstup = int(input("Zadejte nezáporné celé číslo: "))

if vstup < 0:
    print("Chyba: Zadal jste záporné číslo!")
else:
    cislo = vstup
    binarne = ""
    
    if cislo == 0:
        binarne = "0"
    else:
        while cislo > 0:
            zbytek = cislo % 2
            binarne = str(zbytek) + binarne
            cislo = cislo // 2
            
    pocet_bitu = len(binarne)
    pocet_jednicek = binarne.count("1")
    
    print(f"Číslo {vstup} v binárním tvaru je: {binarne}")
    print(f"Počet bitů: {pocet_bitu}")
    print(f"Počet jedniček: {pocet_jednicek}")
    print(f"Kontrola (bin()): {bin(vstup)}")