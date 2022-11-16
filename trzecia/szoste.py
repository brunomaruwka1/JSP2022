i=int(input("Podaj liczbę: "))
for x in range (1,i+1):
    print("".join([f"{j*x:5d}" for j in range (1,11)]))
    
