rzymskie_arabskie={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
liczba="XCVI"
lista=[rzymskie_arabskie[x] for x in liczba]

lista1=[]

print(lista)

for i in range (0,len(lista)-1):
    if lista[i]<lista[i+1]:
        lista[i]*=-1
        lista1.append(lista[i]+lista[i+1])
    lista1.append(lista[i])
        
    
print(lista)
print(lista1)