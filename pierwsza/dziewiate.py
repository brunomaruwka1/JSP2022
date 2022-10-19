import cmath
z=complex(input("Podaj wartosc liczby zespolonej: "))
zmod= abs(z)
zarg=cmath.phase(z)
zcon=z.conjugate()
print(zmod,"\n",zarg,"\n",zcon)