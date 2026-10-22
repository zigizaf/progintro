text = str(input("Zadejte text: "))
bajtu_celkem = 0
i = 0
while i < len(text):
    znak = text[i]
    kod = ord(znak)
    pocet_bajtu = len(znak.encode("utf-8"))
    bajtu_celkem = bajtu_celkem + pocet_bajtu
    print(znak, f"{kod:04X}", pocet_bajtu)
    i = i+1

print (len(text),"znaků", bajtu_celkem, "bajtů" )