import datetime 
today = datetime.date.today()
year = today.year
month = today.month

class Obywatel:
    def __init__(abc,imie,nazwisko,dataUrodzenia):
        abc.imie=imie
        abc.nazwisko=nazwisko
        abc.dU=dataUrodzenia
        abc.dataUrodzenia=(dataUrodzenia.replace("."," ")).split()
        abc.miesiac=int(abc.dataUrodzenia[1])
        abc.rok=int(abc.dataUrodzenia[2])
        if month-abc.miesiac<0:
            abc.wiek=year-abc.rok-1
        if month-abc.miesiac>=0:
            abc.wiek=year-abc.rok
    
    def __str__(abc):
        return(f"Obywatel/ka {abc.imie} {abc.nazwisko}, {abc.wiek} lat, urodzony {abc.dU}")
        
    

osoba=Obywatel("Bruno","Maruwka","5.9.2003")    
print(osoba.__str__())
