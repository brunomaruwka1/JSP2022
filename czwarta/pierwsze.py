print("Hej, nasz program pomoży Ci stworzyć listę liczb naturalnych, a potem wyświetli sumę tych wyrazów i ich iloczyn.")
n=int(input("Ilu wyrazowa ma byc lista?: "))
lista=[]
for i in range(0,n,1):
    x=int(input(f"Podaj {i+1} wyraz listy: "))
    lista.append(x)
print(f"Suma wszystkich wyrazów tego zbioru to: {sum(lista)}")
x=1
for i in lista:
    x*=i
print(f"Iloczyn wszystkich wyrazów tego ciągu {x}")