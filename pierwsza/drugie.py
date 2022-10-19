from cmath import pi
import math

a= int(3)
b= int(4)
kat=int(47)
sinus=round(math.sin((pi/180)*kat),2)
pole=(0.5*a*b*sinus) 
print("Wartosc pola tego trojkata wynosi: ",pole)