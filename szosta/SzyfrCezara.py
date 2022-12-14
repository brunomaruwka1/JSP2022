#a-z = 97-122  ą->ć->ę->ł->ń->ź->ż->ó->ą A-Z=65-90
slowo="Źżęą"
maleLit={'ą':'ć','ć':'ę','ę':'ł','ł':'ń','ń':'ź','ź':'ż','ż':'ó','ó':'ą'}
duzeLit={'Ą':'Ć','Ć':'Ę','Ę':'Ł','Ł':'Ń','Ń':'Ź','Ź':'Ż','Ż':'Ó','Ó':'Ą'}
def szyfrowanie(slowo):
    slowoLista=[ord(x) for x in slowo]
    slowoZaszyfrowane=[]
    for x in slowoLista:
        if x == 122 or x==90:
            slowoZaszyfrowane.append(chr(x-25))
        if x in maleLit:
            slowoZaszyfrowane.append(maleLit(x))
        if x in duzeLit:
            slowoZaszyfrowane.append(duzeLit(x))
        slowoZaszyfrowane.append(chr(x+1))
    return("".join(slowoZaszyfrowane))

def rozszyfrowanie(slowo):
    slowoLista=[ord(x) for x in slowo]
    slowoRozszyfrowane=[]
    for x in slowoLista:
        if x == 97 or x==65:
            slowoRozszyfrowane.append(chr(x+25))
        if x in maleLit:
            slowoRozszyfrowane.append(maleLit(x))
        if x in duzeLit:
            slowoRozszyfrowane.append(duzeLit(x))
        slowoRozszyfrowane.append(chr(x-1))
    return "".join(slowoRozszyfrowane)
        
   
