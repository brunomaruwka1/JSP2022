from itertools import combinations
from itertools import chain

class podzbiory:
    def __init__(abc,zbior):
        abc.zbior=zbior
    def podzbiory(abc):
        dlZbioru=len(abc.zbior)
        podzbiory=[combinations(abc.zbior,i) for i in range(0,dlZbioru+1)]
        podzbiory = [list(i) for i in chain(*podzbiory)]
        return(podzbiory)
                    
zbior=podzbiory([1,2,3,4])
print(zbior.podzbiory())