diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
count = 0
wrong_diameters = 0
for values in (diameters):
    if values < 24.95:
        print(values, "Malý")
        wrong_diameters += 1
    elif values > 25.05:
        print(values, "Velký")
        wrong_diameters += 1
    if values >= 24.95 and values <= 25.05:
        print(values, "OK")
print("Počet nesprávných průměrů:", wrong_diameters)
print("Zmetků:", wrong_diameters/len(diameters) * 100, "%")