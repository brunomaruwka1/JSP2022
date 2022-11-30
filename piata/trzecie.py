rzymskie_arabskie={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
liczba=input("Podaj liczbe rzymska a ja przerobie ja na liczby arabskie: ")
lista=[rzymskie_arabskie[x] for x in liczba]

lista1=[]

print(lista)

for i in range (0,len(lista)-1):
    print(lista1)
    if lista[i]<lista[i+1]:
        lista1.append(-lista[i]+lista[i+1])
        continue
    if lista[i]>lista[i-1] and i>=1:
        continue
    if i==len(lista)-2:
        lista1.extend([lista[i],lista[i+1]])
        break
    lista1.append(lista[i])
    
print(lista)
print(lista1)
print(f"Oto Twoja liczba w zapisie arabskim: {sum(lista1)}")