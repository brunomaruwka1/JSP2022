# sortowanie przez wstawienie
def sortowaniePrzezWstaw(lista):
    for i in range(1,len(lista)):
        wyraz=lista[i]
        j=i-1
        while j>=0 and lista[j]>wyraz:
            lista[j],lista[i]=wyraz,lista[j]
            j-=1
            i-=1
    return(lista)
#sortowanie babelkowe
def sortBombel(lista):
    for i in range(len(lista)):
        for i in range(len(lista)):
            j=i+1
            while j<=len(lista)-1 and i<=len(lista)-2 and lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
                j+=1
                i+=1