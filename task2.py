sekundy=int(input("počet sekund: "))
hodiny=sekundy//3600
minuty=sekundy%3600//60
sekundy=sekundy%3600%60
print(f"{hodiny:02d}:{minuty:02d}:{sekundy:02d}")
