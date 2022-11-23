liczby = {1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'piec',6:'szesc',7:'siedem',8:'osiem',9:'dziewiec',10:'dziesiec',
11:'jedenascie',12:'dwanascie',13:'trzynascie',14:'cztrenascie',15:'pietnascie',16:'szescnacie',17:'siedemnascie',
18:'osiemnacie',19:'dziewietnascie',20:'dwadziescia',30:'trzydziesci',40:'czterdziesci',50:'piedziesiat'}

def liczbaSlownie(liczba):
    if int(liczba)>9:
        return(f"{liczby[int(liczba[0])*10]}-{liczby[int(liczba[1])]}")
    if int(liczba)<=9:
        return(f"{liczby[int(liczba[0])]}")

a=str(input("Podaj numer liczbowo a ja wypisze go slownie: "))
print(liczbaSlownie(a))
print(liczby['jedenascie'])