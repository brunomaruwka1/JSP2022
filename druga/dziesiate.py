lista=[]
for x in range(3,100,3):
    lista.append(x)
print (lista) 
del lista[4:len(lista)-1:3]
print(lista)
print("Średnia arytmetyczna danej listy to",sum(lista)/len(lista))
