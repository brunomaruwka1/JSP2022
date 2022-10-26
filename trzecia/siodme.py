cfibonacciego=[0,1,]
i=1
x=int(input("Podaj jak wiele elementów ciagu Fibonacciego mam napisac:" ))
while i<x-1:
    a=cfibonacciego[-1] + cfibonacciego[-2]
    cfibonacciego.append(a)
    i+=1
print(cfibonacciego)
