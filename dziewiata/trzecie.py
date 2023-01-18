import numpy as np
import matplotlib.pylab as plt

Vo=int(input("Podaj predkosc poczatkowa[m/s]: "))
alfa=int(input("Kat: "))

g=9.81
Vy=Vo*round(np.sin((alfa/180)*np.pi),3)
Vx=Vo*round(np.cos((alfa/180)*np.pi),3)
print(f"{Vy}  {Vx}")

zasieg=round(2*Vx*Vy/g,2)
wysokosc=round((Vy**2)/(2*g),2)
czas=round(2*Vy/g,2)
print(f"Zasieg:{zasieg}\nWysokosc:{wysokosc}\nCzas:{czas}")

plt.subplot(1,3,1)
t = np.linspace(0, 2*czas, 1000)
a=-wysokosc/(czas**2)
plt.plot(t, a*(t-2*czas)*t)
plt.xlabel('t[s]')
plt.ylabel('y(t)[m]')
plt.axis('tight')


plt.subplot(1,3,2)
t=np.linspace(0,2*czas,1000)
Vy=Vy-g*t
Vx=[Vx for i in range(1000)]
plt.plot(t,Vx,t,Vy)
plt.xlabel('t[s]')
plt.ylabel('y(t)[m]')
plt.axis('tight')


plt.subplot(1,3,3)
x=np.linspace(0,zasieg,1000)
a=wysokosc/((0.5*zasieg-zasieg)*(0.5*zasieg))
y=a*(x-zasieg)*x
plt.plot(x,y)
plt.xlabel('t[s]')
plt.ylabel('y(t)[m]')
plt.axis('tight')

print(a)

plt.show()



