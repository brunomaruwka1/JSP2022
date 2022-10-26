haslo=str(input("Wpisz nowe hasło:"))
B=0 #licznik malych liter 65-90
A=0 #licznik duzych liter 97-122
C=0 #licznik znaków specjalnych 36,35,64
D=0 #dlugosc hasla
E=0 #liczba cyfr
znakiszcz=["$","#","@"]
for x in haslo:
    if ord(x)>=65 and ord(x)<=90:
        A+=1
    if ord(x)>=97 and ord(x)<=122:
        B+=1
    if x==znakiszcz[0 or 1 or 2]:
        C+=1
    if len(haslo)>=6 and len(haslo)<=16:
        D+=1
    if ord(x)>=48 and ord(x)<=57:
        E+=1
if A>=1 and B>=1 and C>=1 and D>=1 and E>=1:
    print("To hasło jest wystarczająco silne")
elif A==0:
    print("Hasło nie posiada żadnej dużej litery")
elif B==0:
    print("Hasło nie posiada żadnej małej litery")
elif C==0:
    print("Hasło nie posiada żadnego ze znaków specjalnych")
elif len(haslo)<6:
    print("To hasło jest za krótkie")
elif haslo>15:
    print("To haslo jest za dlugie")
elif E==0:
    print("Hasło nie posiada żadnych cyfr")
