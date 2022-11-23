liczby = {0:"",1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'piec',6:'szesc',7:'siedem',8:'osiem',9:'dziewiec',10:'dziesiec',
11:'jedenascie',12:'dwanascie',13:'trzynascie',14:'cztrenascie',15:'pietnascie',16:'szescnacie',17:'siedemnascie',
18:'osiemnacie',19:'dziewietnascie',20:'dwadziescia',30:'trzydziesci',40:'czterdziesci',50:'piedziesiat',60:'szescdziesiat',
70:'siedemdziesiat',80:'osiemdziesiat',90:'dziewiecdziesiat',100:'sto',200:'dwiescie',300:'trzysta',400:'czterysta',
500:'piecset',600:'szescset',700:'siedemset',800:'osiemset',900:'dziewiecset',1000:'tysiac'}

liczba=input("Podaj liczbe z przedzialu(1-1999) zapisana dziesietnie a ja napisze Ci ja slownie: ")
 
for x in range(-len(liczba),0):
    if int(x)==-2 and len(liczba)>=2 and int(liczba[-2])<2:
        print(liczby[int(liczba[-2])*10**(abs(x)-1)+int(liczba[-1])*10**(abs(x))-2],end=" ")
    print(liczby[int(liczba[x])*10**(abs(x)-1)],end=" ")
            

    

    



