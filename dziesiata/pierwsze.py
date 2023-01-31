import math
class Kolo:
    def __init__(abc,promien):
        abc.promien=promien     
    def poleKola(abc):
        return abc.promien**2*math.pi
    def obwodKola(abc):
        return abc.promien*2*math.pi

pKolo=Kolo(5)
print(pKolo.obwodKola())
print(pKolo.poleKola())