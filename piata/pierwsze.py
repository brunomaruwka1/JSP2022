wartosci = {"zero": 0,"jeden": 1,"dwa": 2,"trzy": 3,"cztery": 4,"piec": 5,"szesc": 6,"siedem": 7,"osiem": 8,"dziewiec": 9,
"dziesiec": 10,"jedenascie": 11,"dwanascie": 12,"trzynascie": 13,"czternascie": 14,"pietnascie": 15,"szesnascie": 16,
"siedemnascie": 17,"osiemnascie": 18,"dziewietnascie": 19,"dwadziescia": 20,"trzydziesci": 30,
"czterdziesci": 40,"piecdziesiat": 50,}

liczba=input("Podaj liczbe z przedzialu (1-59) slownie a ja ją podam w zapsie dziesietnym: ")
suma=0
for x in (liczba.split()):
    suma+=wartosci[x]
print(suma) 