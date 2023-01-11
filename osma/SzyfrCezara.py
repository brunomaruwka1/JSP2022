#a-z = 97-122 A-Z=65-90
slowo="Źżęą"
maleLit={'ą':'ć','ć':'Ą','ę':'ł','ł':'ę','ń':'ź','ź':'ń','ż':'ó','ó':'ż'}
duzeLit={'Ą':'Ć','Ć':'Ą','Ę':'Ł','Ł':'Ę','Ń':'Ź','Ź':'Ń','Ż':'Ó','Ó':'Ż'}

def szyfrowanie(slowo,n=1):
    slowoZaszyfrowane=[]
    for x in slowo:
        if (ord(x)>=97 and ord(x)<=122 and ord(x)+n >= 122) or (ord(x) >= 65 and ord(x)<=90 and ord(x)+n>=90):
            slowoZaszyfrowane.append(chr(ord(x)+n-26))
            continue 
        elif (ord(x)>=97 and ord(x)<=122)or(ord(x) >= 65 and ord(x)<=90):
            slowoZaszyfrowane.append(chr(ord(x)+n))
            continue
        slowoZaszyfrowane.append(x)
    return("".join(slowoZaszyfrowane))

def rozszyfrowanie(slowo,n=1):
    slowoRozszyfrowane=[]
    for x in slowo:
        if (ord(x)>=97 and ord(x)<=122 and ord(x)-n < 97) or (ord(x) >= 65 and ord(x)<=90 and ord(x)-n<65):
            slowoRozszyfrowane.append(chr(ord(x)+26-n))
            continue
        elif (ord(x)>=97 and ord(x)<=122)or(ord(x) >= 65 and ord(x)<=90):
            slowoRozszyfrowane.append(chr(ord(x)-n))
            continue
        slowoRozszyfrowane.append(x)
    return "".join(slowoRozszyfrowane)



print(rozszyfrowanie("Vq lguv vgmuv fq bcubahtqycpkc",2))
   
