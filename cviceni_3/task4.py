hodnoty= [8,16,32,64]
for bity in hodnoty:
    u_min=0
    u_max=(2**bity)-1

    s_min=-(2**(bity-1))
    s_max=(2**(bity-1))-1
    print(f"Počet bitů: {bity},: {u_min}, až: {u_max}, bez zanaménka: {s_min} až {s_max}")