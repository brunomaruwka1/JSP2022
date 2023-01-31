def dzielniki(liczba):
    dzielniki=[i for i in range(1,liczba+1) if liczba%i==0]
    return(dzielniki)


def lPierwsza():
    if dzielniki(liczba)==[1,liczba]:
        return("to jest l.pierwsza")

def lDoskonala():
    if sum(dzielniki(liczba))-liczba==liczba:
        return("To jest liczba doskonala")

try:
    liczba=int(input("Podaj liczbe: "))
    print(f"{dzielniki(liczba)}\n{lPierwsza()}\n{lDoskonala()}")
except ValueError:
    print("To nie jest liczba calkowita!")