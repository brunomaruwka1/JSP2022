import time

def ciagFibo1(n):
    lista=[0,1]
    for x in range(2,n):
        lista.append(lista[x-1]+lista[x-2])
    return(lista[-1])



def ciagFibo2(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else: 
        return ciagFibo2(n-1)+ciagFibo2(n-2)

czas1 = time.time()
czas1 = time.time()
print(ciagFibo1(10000))
czas2 = time.time()
print(ciagFibo2(30))
czas3 = time.time()
print(f"Czas przez iteracje: {czas2-czas1}\nCzas przez rekurencje: {czas3-czas2}")
