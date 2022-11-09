listalicz=[]
n=int(input("Ile elemntów ma mieć lista?: "))
for x in range(0,n):
    element=int(input(f"Podaj {x+1} elemnt: "))
    listalicz.append(element)
listalicz.sort()
if n%2==0:
    mediana=(listalicz[len(listalicz)//2-1]+listalicz[-len(listalicz)//2])/2
    print(f"Mediana to {mediana}")
elif n%2==1:
    mediana=listalicz[-len(listalicz)//2]
    print(f"Mediana to {mediana}")
