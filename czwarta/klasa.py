listaosob=[]
n=int(input("Ile osob jest w klasie? "))
for i in range (0,n,1):
    osoba=str(input(f"Podaj {i+1} imię osoby: "))
    listaosob.append(osoba)
listaosob.sort()
for x in listaosob:
     print(f"({listaosob.index(x)+1}) {x}")