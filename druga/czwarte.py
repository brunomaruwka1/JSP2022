import sys

a=list(input("Podaj słowo: "))
i=1
while i< len(a):
    if a[i]==a[0]:
        a[i]="$"
    i+=1 
for y in a:
    sys.stdout.write(y)

    

        
