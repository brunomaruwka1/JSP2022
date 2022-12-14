#a-z = 97-122 A-Z=65-90
slowo="Źżęą"
maleLit={'ą':'ć','ć':'Ą','ę':'ł','ł':'ę','ń':'ź','ź':'ń','ż':'ó','ó':'ż'}
duzeLit={'Ą':'Ć','Ć':'Ą','Ę':'Ł','Ł':'Ę','Ń':'Ź','Ź':'Ń','Ż':'Ó','Ó':'Ż'}
def szyfrowanie(slowo):
    slowoZaszyfrowane=[]
    for x in slowo:
        if ord(x) == 122 or ord(x)==90:
            slowoZaszyfrowane.append(chr(ord(x)-25))
            continue
        if x in maleLit.keys():
            slowoZaszyfrowane.append(maleLit[x])
            continue
        if x in duzeLit.keys():
            slowoZaszyfrowane.append(duzeLit[x])
            continue
        slowoZaszyfrowane.append(chr(ord(x)+1))
    return("".join(slowoZaszyfrowane))

def rozszyfrowanie(slowo):
    slowoRozszyfrowane=[]
    for x in slowo:
        if ord(x) == 97 or ord(x)==65:
            slowoRozszyfrowane.append(chr(ord(x)+25))
            continue
        if x in maleLit.keys():
            slowoRozszyfrowane.append(maleLit[x])
            continue
        if x in duzeLit.keys():
            slowoRozszyfrowane.append(duzeLit[x])
            continue
        slowoRozszyfrowane.append(chr(ord(x)-1))
    return "".join(slowoRozszyfrowane)
    
print(szyfrowanie("róża"))
   
