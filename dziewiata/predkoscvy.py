import numpy as np
czasy=[]
t=np.linspace(1,8.16,1000)
for i in t:
    czasy.append(i)
print(czasy)
g=9.81
czas=4.08
Vy=20
print(t[0])
VY=[]
for i in czasy:
    if i <= czas:
        VY.append(Vy-g*i)
    if i > czas:
        VY.append(g*(i-czas))
print(VY)