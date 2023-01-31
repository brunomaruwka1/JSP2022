import time
import sortowanie
import random

def tworzenieList(liczbaElementow):    
    lista=[]
    for i in range(liczbaElementow):
        lista.append((random.randint(1,20)))
    return(lista)

listaDoPosortowania=tworzenieList(5000)

czas1=time.time()
sortowanie.sortBombel(listaDoPosortowania)
czas2=time.time()
czas3=time.time()
sortowanie.sortowaniePrzezWstaw(listaDoPosortowania)
czas4=time.time()

print(f"Czas sortowania listy przez sort. babelkowe to {czas2-czas1}, a przez wstawianie to {czas4-czas3}.")
