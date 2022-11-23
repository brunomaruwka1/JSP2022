lista=[]
n=int(input("numer:"))
for i in range(1,n+1):
    wiersz=[]
    for x in range (1,i+1):
        if x==1 or x==i:
            wiersz.append(1)
        elif x!=0 and x!=n:
                wiersz.append(lista[i-2][x-2]+lista[i-2][x-1])
    lista.append(wiersz)
# print(lista)
for b in lista: 
    print(" "*(n-lista.index(b)-1)+"".join(str(b)))