
class Zespolona:
    i=(-1)*(1/2)

    def __init__(self, re, im):
        self.re=re
        self.im=im

    def show(self):
        print(f"{self.re}+i{self.im}")

    def dodaj(a,b):
        if a.im+b.im<0:
            print(f"{a.re+b.re}{a.im+b.im}i")
        if a.im+b.im>0:
            print(f"{a.re+b.re}+{a.im+b.im}i")
        if a.im+b.im==0:
            print(f"{a.re+b.re}")
        if a.re+b.re==0:
            print(f"{a.im+b.im}i")
    
    def odejmij(a,b):
        if a.im-b.im<0:
            print(f"{a.re-b.re}{a.im-b.im}i")
        if a.im-b.im>0:
            print(f"{a.re-b.re}+{a.im-b.im}i")
        if a.im-b.im==0:
            print(f"{a.re-b.re}")
        if a.re-b.re==0:
            print(f"{a.im-b.im}i")
    
    def mnoz(a,b):
        print(f"{a.re*b.re-a.im*b.im}+{a.re*b.im+b.re*a.im}i")

    def modul(a):
        print((a.re**2+a.im**2)**(1/2))

a= Zespolona(3,4)
b= Zespolona(2,3)

Zespolona.dodaj(a,b)
Zespolona.odejmij(a,b)
Zespolona.modul(a)
Zespolona.modul(b)