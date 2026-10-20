n = int(input("Zadejte číslo: "))
prvocislo = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        prvocislo = False
        break
        
if prvocislo:
   print (n, "je prvocislo")
else:
    print (n, "není prvočíslo")

faktory = []
delitel = 2

m = n
while m > 1:
  while m % delitel == 0:
    faktory.append(delitel)
    m //= delitel
  delitel += 1
print ("rozklad čísla", n, "je", faktory)
   

prvocisla = []
for cislo in range(2, 100):
  for i in range(2, int(cislo**0.5) + 1):
    if cislo % i == 0:
      break
  else:
    prvocisla.append(cislo)
print (prvocisla)
print (len(prvocisla), "prvočísel je menších než 100")