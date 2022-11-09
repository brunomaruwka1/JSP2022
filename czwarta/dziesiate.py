def szukanie_dzielnikow(x, listliczb, listdzielnikow,j=0):
    while  x+1>listliczb[j]:
        if x%listliczb[j]==0:
            listdzielnikow.append(lista[j])
            listdzielnikow.sort()
        j+=1
lista=[]
for d in range (1,1000):
    lista.append(d)
    d+=1

dzielniki_a=[]
dzielniki_b=[]
wspolnedzielniki=[]
a=int(input("Podaj dwie liczby całkowite a my pomożemy Ci znaleźć ich wspólny najwikeszy dzielnik\nPodaj wartość pierwszej liczby: "))
b=int(input("Podaj wartośc drugiej liczby: "))
i=0
szukanie_dzielnikow(a,lista,dzielniki_a)
szukanie_dzielnikow(b,lista,dzielniki_b)
#print(f"Dzielniki pierwszej liczby to: {dzielniki_a}")
#print(f"Dzielniki drugiej liczby to: {dzielniki_b}")
for i in dzielniki_a:
    for j in dzielniki_b:
        if i==j:
            wspolnedzielniki.append(i)
print(f"Największy wspólny dzielnik obydwu tych liczb to {max(wspolnedzielniki)}")
