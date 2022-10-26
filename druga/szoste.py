studentlist=["Kasia","Basia","Marek","Darek"]
studentlist.append("Józek")
studentlist.sort()
print(studentlist)
print(studentlist[3],studentlist[:2],studentlist[-2:])
studentlist.remove("Basia")
print(studentlist)
print(tuple(studentlist))