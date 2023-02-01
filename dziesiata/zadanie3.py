from itertools import combinations
from random import randint

class podlisty:
    def __init__(self, lista):
        self.lista = lista
    def tworzPodlist(self):
        kombinacje = list(combinations(self.lista,3))
        wyniki=[list(i) for i in kombinacje if sum(i)==0]
        return(wyniki)

test = podlisty([1, -3, 4, 1, 2, 0, 7, 2, 5, -2, -4, -1])
print(test.tworzPodlist())
