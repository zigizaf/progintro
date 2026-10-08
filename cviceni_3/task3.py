slovo=str(input("Zadej slovo: "))
pocet_pismen=len(slovo)
prvni_pismeno=slovo[0]
posledni_pismeno=slovo[-1]
velka_pismena=slovo.upper()
pozpatku=slovo[::-1]
palindorom=slovo==pozpatku
print(f"Zadané slovo je: {slovo}")
print(f"Počet písmen ve slově: {pocet_pismen}")
print(f"První písmeno: {prvni_pismeno}")
print(f"Poslední písmeno: {posledni_pismeno}")  
print(f"Slovo velkými písmeny: {velka_pismena}")
print(f"Slovo pozpátku: {pozpatku}")
if palindorom:
    print("True")
else:
    print("False")
