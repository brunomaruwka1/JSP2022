nazwaPliku=input("Podaj nazwe pliku:")
try:
    tekst=open(f"{nazwaPliku}.txt","r")
    pali=open(f"palindromy.txt","a")
    niePali=open(f"nie_palindromy.txt","a")
    
    with open('tekst.txt') as f:
        for line in f.readlines():
            print(line.strip())
            if line.strip()==line.strip()[::-1]:
                pali.write(f"{line}\n")
            else:
                niePali.write(f"{line}\n")
    niePali.close()
except(FileNotFoundError):
    print("Blad! Nie istnieje taki plik. ")