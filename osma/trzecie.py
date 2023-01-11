from random import randint

def tworzeniePeselu():
    rok_urodzenia=str(randint(1922,2022))
    miesiac_urodzenia=str(randint(1,12))

    if int(miesiac_urodzenia) in [1,3,5,7,8,10,12]:
        dzien_urodzenia=randint(1,31)
    elif int(miesiac_urodzenia) in [4,6,9,11]:
        dzien_urodzenia=randint(1,30)
    elif int(miesiac_urodzenia)==2:
        dzien_urodzenia=randint(1,28)

    if randint(1,2)==1:
        plec="mezczyzna"
        numer_plci=randint(0,4)*2+1
    else:
        plec="kobieta"
        numer_plci=randint(0,4)*2

    if int(rok_urodzenia)>1999:
        rok_pesel=rok_urodzenia[2:4]
        miesiac_pesel=str(int(miesiac_urodzenia)+20)
    if int(rok_urodzenia)<=1999:
        rok_pesel=rok_urodzenia[2:4]
        if int(miesiac_urodzenia)<10:
            miesiac_pesel=f"0{miesiac_urodzenia}"
        else: 
            miesiac_pesel=miesiac_urodzenia

    if int(dzien_urodzenia)<10:
        dzien_urodzenia=f"0{dzien_urodzenia}"

    trzy_losowe=f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"

    pesel=f"{rok_pesel}{miesiac_pesel}{dzien_urodzenia}{trzy_losowe}{numer_plci}"

    waga=[1,3,7,9,1,3,7,9,1,3]

    liczba_kontrolna=0

    for i in range(10):
        liczba_kontrolna+=int(str(int(pesel[i])*waga[i])[-1])
    liczba_kontrolna=str(10-int(str(liczba_kontrolna)[-1]))
        
    if int(liczba_kontrolna)==10:
        liczba_kontrolna="0"    

    pesel=f"{rok_pesel}{miesiac_pesel}{dzien_urodzenia}{trzy_losowe}{numer_plci}{liczba_kontrolna}"
    return pesel
    #print(pesel)
    #print(f"{dzien_urodzenia}-{miesiac_urodzenia}-{rok_urodzenia}-{plec}")

