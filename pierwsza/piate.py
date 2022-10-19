import math

print(5//2)
#dzielenie liczb bez reszty zaokrągla wynik działania w dół do nabliższej liczby całkowitej
print(round(float(11/2)))
#gdy jest liczba <5, po przecinku zaokragla w dol,gdy >5 zaokragla w gore a gdy po przecinku znajduje sie 5 to:
#zaokragla w dol jesli liczba przed przecinkiem jest parzysta, w gore jesli liczba przed przecinkiem jest nieparzysta
print(math.floor(float(5/2)))
#zaokrąga w dół do najblższej liczby całkowitej
print(round(float(52.6)))
print(round(float(53.4)))