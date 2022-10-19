from cmath import pi
import math

a=int(input("Podaj dlugosc boku a: "))
b=int(input("Podaj dlugosc boku b: "))
kat=int(input("Podaj wartosc kata miedzy bokami a i b: "))
sinus=round(math.sin((pi/180)*kat),2)
pole=(0.5*a*b*sinus) 
print("Wartosc pola tego trojkata wynosi: ",pole)
