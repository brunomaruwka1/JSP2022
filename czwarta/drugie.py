def usuwanie_tych_samych_wyrazow(*list):
    for x in lista:
        for y in lista:
            if x==y:
                lista.remove(y)

n=int(input("Ilu wyrazowa ma byc lista?: "))
lista=[]
for i in range(0,n,1):
    x=int(input(f"Podaj {i+1} wyraz listy: "))
    lista.append(x)
usuwanie_tych_samych_wyrazow(lista)
print(lista)    