lista=[]
wiersz=[]
n=int(input("numer:"))
for i in range(1,n+1):
    wiersz=[]
    for x in range (1,i+1):
        if x==1 or x==i:
            wiersz.append(1)
        elif x!=0 and x!=n:
                print(lista[n-2][x-1]+lista[n-2][x])
                wiersz.append(lista[n-2][x-1]+lista[n-2][x])
        print(lista)
    lista.append(wiersz)
    print(lista)