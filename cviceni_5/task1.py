def circle_area(d):
    r = d/2
    S = 3.14*r**2
    return S

obsah_kruhu = circle_area(4)
print (obsah_kruhu)

def tube_cross_section(d_out, d_in):
    vnitrni_prumer = circle_area(d_in)
    vnejsi_prumer = circle_area(d_out)
    return vnitrni_prumer, vnejsi_prumer
obsah_prurezu = tube_cross_section(4,2)
print (obsah_prurezu)

def tube_mass(d_out, d_in, length, density=7850):
    vnitrni_prumer = circle_area(d_in)
    vnejsi_prumer = circle_area(d_out)
    prurez = vnejsi_prumer - vnitrni_prumer
    obsah_materialu_trubky = prurez * length
    hmotnost = obsah_materialu_trubky * density
    return hmotnost
hmotnost_trubky = tube_mass(0.060, 0.050, 6)
print (hmotnost_trubky)
print(tube_mass(0.060, 0.050, 6, density=2700))