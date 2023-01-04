import random
import time

def tworzenieList(liczbaElementow):    
    lista=[]
    for i in range(liczbaElementow):
        lista.append((random.randint(1,20)))
    return(lista)

def sortowanieListy(lista):
    for i in range(1,len(lista)):
        wyraz=lista[i]
        j=i-1
        while j>=0 and lista[j]>wyraz:
            lista[j],lista[i]=wyraz,lista[j]
            j-=1
            i-=1
    return(lista)

a=tworzenieList(1000)
b=tworzenieList(2000)
c=tworzenieList(3000)

czas1=time.time()
sortowanieListy(a)
czas2=time.time()
sortowanieListy(b)
czas3=time.time()
sortowanieListy(c)
czas4=time.time()

print(f"Czas sortowania listy 1000-elementowej: {(czas2-czas1)}\nCzas sortowania listy 2000-elementowej: {czas3-czas2}\nCzas sortowania listy 3000-elementowej: {czas4-czas3}")