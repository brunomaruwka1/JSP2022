lista=[]
wiersz=[]
n=int(input("numer: "))
for y in range(1,n+1): 
    print(y)
    for x in range(0,y):
        if x==1 or x==y:
            wiersz[x]=1
        elif x!=1 and x!=n:
            print(lista[y-2][x-2]+lista[y-2][x-2])
            wiersz.append(lista[y-2][x-2]+lista[y-2][x-2])
    lista.append(wiersz)
    print(wiersz)
    print(lista)
    wiersz.clear()
print(lista)