import trojkat

print('Podaj dlugosci kata a ja podam Ci informacje o nim.')
a=int(input('Podaj dl. 1. boku: '))
b=int(input('Podaj dl. 2. boku: '))
c=int(input('Podaj dl. 3. boku: '))
if a+b<c or a+c<b or b+c<a:
    print("To nie jest trojkat")
print(trojkat.obwodTroj(a,b,c))
print(trojkat.poleTroj(a,b,c))
print(trojkat.rodzajTrojBok (a,b,c))
print(trojkat.rodzajTrojKat (a,b,c))