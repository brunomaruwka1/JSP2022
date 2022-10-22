from itertools import chain

#help(chain)
listapoczatkowa=[[2,4,3],[1,5,6],[9],[7,9,0]]
listakoncowa=list(chain(*listapoczatkowa))
print(listakoncowa)
