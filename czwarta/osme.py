n=int(input("Sume ilu elementow szeregu hamronicznego mam obliczyc?: "))
i=0
for x in range(1,n+1,1):
    i+=1/x
print(round(i,3))