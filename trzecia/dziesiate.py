lista=[]
lista1=[]
for i in range(100,401,1):
    lista.append(str(i))
for i in lista:
        if int(i[0])%2==0 and int(i[1])%2==0 and int(i[2])%2==0 :
            lista1.append(i)
lista11=",".join(lista1)
print(lista11)