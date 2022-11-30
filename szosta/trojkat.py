def obwodTroj(a,b,c):
    return(f"Obwod trojkata to : {a+b+c}")

def poleTroj(a,b,c):
    p=(a+b+c)/2
    return (f'Pole trojkata to : {(p*(p-a)*(p-b)*(p-c))**(1/2)}')

def rodzajTrojBok (a,b,c):
    if a==b==c:
        return('Trojkat jest rownoboczny')
    if a==b or b==c or a==c:
        return('Trojkat jest rownoramienny')
    if a!=b and a!=c and b!=c: 
        return('Trojkat jest roznoboczny')

def rodzajTrojKat (a,b,c):
    boki=[a,b,c]
    boki.sort()
    kwMniej=a**2+b**2
    if kwMniej<c**2:
        return('Trojkat jest rozwartokatny')
    if kwMniej>c**2:
        return('Trojkat jest ostrokatny')
    if kwMniej==c**2:
        return('Trojkat jest prostokatny')
    



print(rodzajTrojKat(4,3,2))
