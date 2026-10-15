počet=0
for i in range(1890, 2031):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        počet += 1
print("Počet přestupných let mezi 1890 a 2030 je:", počet)        
rok = int(input("Zadejte rok: "))
if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print(rok, "je přestupný rok.")
else:
    print(rok, "není přestupný rok.")    