klucz={'a':'y','e':'i','i':'o','o':'a','y':'e'}
slowo=input("Podaj slowo a my je odpowiednio zaszyfrujemy aby nikt nie mogl go rozkodowac: ")
lista=[]
for x in slowo:
    if x in "aeioy":
        lista.append(klucz[x])
        continue
    lista.append(x)
print ("".join(lista))