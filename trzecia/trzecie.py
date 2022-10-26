print("Hej!Przy uzyciu tego programu pomozemy znalezc Ci miejsca zerowe rownania kwadratowego ax**2+bx+c=0 ")
a = int(input("Podaj wartosc a: "))
if a==0:
    print("To nie jest równanie kwadratowe.")
else:
    b = int(input("Podaj wartosc b: "))
    c = int(input("Podaj wartosc c: "))
    delta= float((b**2)-4*a*c)
    if delta>1:    
        pp=(-b-(delta**(1/2)))/2*a
        dp=(-b+(delta**(1/2)))/2*a
        print("Pierwsze rozwiazanie to: ",pp,"drugie to: ",dp)
    if delta==0:
        p=-b/2*a
        print("Równanie ma rozwiazanie w punkcie",p)
    else:
        print("Równanie nie ma rozwiazan")