from czwarte import infoPesel

pesele=open("PESELE.txt","r")
peseleO=open("PESELE_ODCZYTANE.txt","w")

# tekst=pesele.readline()
with open('PESELE.txt') as f:
    for line in f.readlines():
        peseleO.write(f"{infoPesel(str(line.strip()))}\n")
        # print(str(line.strip()))

pesele.close()
peseleO.close()

# print(tekst)