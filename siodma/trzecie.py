import random
import time

def tworzenieList(liczbaElementow):    
    lista=[random.randint(1,20) for i in range(liczbaElementow)]
    return(lista)


def sortBombel(lista):
    for i in range(len(lista)):
        for i in range(len(lista)):
            j=i+1
            while j<=len(lista)-1 and i<=len(lista)-2 and lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
                j+=1
                i+=1
                
    return lista

a=tworzenieList(1000)
b=tworzenieList(2000)
c=tworzenieList(3000)

czas1=time.time()
sortBombel(a)
czas2=time.time()
sortBombel(b)
czas3=time.time()
sortBombel(c)
czas4=time.time()

print(f"Czas sortowania listy 1000-elementowej: {(czas2-czas1)}\nCzas sortowania listy 2000-elementowej: {czas3-czas2}\nCzas sortowania listy 3000-elementowej: {czas4-czas3}")