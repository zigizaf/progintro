n = int(input("Zadejte celé liché číslo: "))
if n > 0 and n % 2 != 0:
    stred = n // 2
    for i in range(n):
        mezery = abs(stred - i)
        hvezdicky = n - 2 * mezery
        print(" " * mezery + "*" * hvezdicky)
else:
    print ("Chyba! Musíš zadat liché a kladné číslo. Zkus to znovu")

