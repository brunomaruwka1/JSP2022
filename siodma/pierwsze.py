def ciagFibo1(n):
    lista=[0,1]
    for x in range(2,n):
        lista.append(lista[x-1]+lista[x-2])
        print(lista)

ciagFibo1(8)

def ciagFibo2(n):
    if n>2:
        return ciagFibo2(n-1)+ciagFibo2(n-2)
    if n==2:
        return 1

print(ciagFibo2(4))