class Item:
    def __init__(self, name, unit_price, quantity):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
class Warehouse:
    def __init__(self):
        self.items = []
    def find(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None
            
    def add(self, name, unit_price, quantity ):
        item = self.find(name)
        if item:
            item.quantity += quantity
        else:
            self.items.append(Item(name, unit_price, quantity))

    def remove(self, name, quantity):
        item = self.find(name)
        if item and item.quantity >= quantity:
            item.quantity -= quantity
            return True
        else:
            return False

    def total_value(self):
        celkem = 0
        for item in self.items:
            celkem += item.unit_price * item.quantity
        return celkem

    def low_stock(self, limit):
        seznam = []
        for item in self.items:
            if item.quantity < limit:
                seznam.append(item.name)
        return seznam
    def report(self):
        for item in self.items:
            print(item.name, item.quantity, item.unit_price,"Kč/ks")
        print(self.total_value(),"Kč")    

sklad = Warehouse()
# 1. Naplnění skladu
sklad.add("Jablka", 25, 100)
sklad.add("Hrušky", 35, 40)
sklad.add("Mléko", 22, 15)

# Opakované přidání Mléka (navýší množství na 25)
sklad.add("Mléko", 22, 10)

print("Počáteční stav skladu:")
sklad.report()

# 2. Výdej zboží (úspěšný i neúspěšné)
print("Výdej 30 Jablek:", sklad.remove("Jablka", 30))       # True (úspěch)
print("Výdej 50 Mléka (nedostatek):", sklad.remove("Mléko", 50))  # False
print("Výdej 5 Banánů (neexistuje):", sklad.remove("Banány", 5))  # False
print()

# 3. Kontrola nízkého stavu
print("Položky pod 20 ks:", sklad.low_stock(20))
print()

# 4. Závěrečný přehled
print("Závěrečný stav skladu:")
sklad.report()