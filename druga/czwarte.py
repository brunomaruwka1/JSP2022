a=list(input("Podaj słowo: "))
i=1
while i< len(a):
    if a[i]==a[0]:
        a[i]="$"
    i+=1 
a="".join(a)
print(a)

    

        
