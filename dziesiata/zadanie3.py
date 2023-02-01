from itertools import combinations
from random import randint

class podlisty:
    def __init__(self, lista):
        self.lista = lista
    def tworzPodlist(self):
        wyniki=[k for k in list(combinations(self.lista,3)) if sum(k)==0]
        return(wyniki)

test = podlisty([1, -3, 4, 1, 2, 0, 7, 2, 5, -2, -4, -1])
print(test.tworzPodlist())
