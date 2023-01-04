import time 
#Ciąg poprzez rekurencję
N = int(input("Ile wyrazow ciągu Fibonacciego chcesz wyznaczyć: "))
def rekurencyjnie(N):
    wyraz = [0,1]
    suma = 0
    print("1 wyraz ciągu Fibonacciego to: 0")
    for x in range(1,N):
        wyraz[0] = wyraz[1]
        wyraz[1] = suma
        suma = wyraz[0] + wyraz[1]
        print(x+1, "wyraz ciągu Fibonacciego to:", suma)    
#Ciąg poprzez iteracje0
def pętla(N):
    n = 2
    a = n - 2
    b = n - 1
    print("1 wyraz ciągu Fibonacciego to: 0")
    for i in range(1,N):
        b += a
        a = b - a
        print(i+1, "wyraz ciągu Fibonacciego to:", a)

bla={"a":"b"}
print(bla.keys())