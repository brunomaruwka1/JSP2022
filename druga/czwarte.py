from ntpath import join

a=list(input("Podaj słowo: "))
i=1
while i< len(a):
    if a[i]==a[0]:
        a[i]="$"
    i+=1 
print("".join(a))

    

        
