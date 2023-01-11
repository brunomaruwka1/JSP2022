from trzecie import tworzeniePeselu as newPesel

pesele=open("PESELE.txt","w")

for i in range(40):
    if pesele.writable():
        pesele.write(f"{newPesel()}\n")

pesele.close()