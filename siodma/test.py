#klasa=[{"imie":"Bruno","nazwisko":"Maruwka"},{"imie":"Ed","nazwisko":"JO"}]
plik=open("listauczniocw.txt","w")

n=int(input("Podaj liczbe uczniow:"))

klasa=[{"imie":input("Podaj imie: "),"nazwisko":input("Podaj nazwisko: ")} for x in range(0,n)]

klasa=sorted(klasa, key=lambda x: x['nazwisko'])
print(klasa)

for i in klasa:    
    plik.write((f"{klasa.index(i)+1:2d} {i['imie']} {i['nazwisko']}\n"))

plik.close()