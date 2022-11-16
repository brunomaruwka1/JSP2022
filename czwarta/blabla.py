lista=[[1],]
n=2
for y in range(0,n):
    wiersz=[]
    for x in range (0,y):
        if x==0 or x==1 :
            wiersz.append(1)
            print(wiersz)
        elif x!=0 and x!=n and y!=1:
                print(lista[y-1][x-1]+lista[y-1][x])
                wiersz.append(lista[y-1][x-1]+lista[y-1][x])
        lista.append(wiersz)
    print(lista)