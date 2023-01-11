def infoPesel(pesel):
    if int(pesel[2:4])>12:
        mUrodzenia=int(pesel[2:4])-20
        rUrodzenia=int(pesel[0:2])+2000
    elif int(pesel[2:4])<=12:
        mUrodzenia=int(pesel[2:4])
        rUrodzenia=int(pesel[0:2])+1900

    dUrodzenia=pesel[4:6]


    if int(pesel[9])%2==1:
        plec="mezczyzna"
    elif int(pesel[9])%2==0:
        plec="kobieta"

    def liczbaKontrolna(pesel,waga=[1,3,7,9,1,3,7,9,1,3]):
        liczbaKontrolna=0
        for i in range(10):
            liczbaKontrolna+=int(str(waga[i]*int(pesel[i]))[-1])
        liczbaKontrolna=str(10-int(str(liczbaKontrolna)[-1]))
        liczbaKontrolna=liczbaKontrolna[-1]
        return liczbaKontrolna

    if mUrodzenia<10:
        mUrodzenia=f"0{str(mUrodzenia)}"

    if pesel[-1]==liczbaKontrolna(pesel):
        # print('Pesel prawdilowy')
        return f"nr PESEL:{pesel}\tdata urodzenia {dUrodzenia}-{mUrodzenia}-{rUrodzenia};\t plec:{plec}"
    else:
        return ("Pesel nieprawdilowy")
        


