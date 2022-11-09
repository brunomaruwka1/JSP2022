from cmath import pi


x = int(input("Hej pomoge Ci przekonwertowac stopnie na radiany lub odwrtotnie.\n(0-stopnir na radiany, 1-odwrotnie): "))
if x==0:
    stopnie=float(input("Podaj wartośc kąta w stopniach: "))
    radiany=stopnie*2/180
    print(f"Ten kąt w radianach ma wartość:{round(radiany,2)}pi")
elif x==1:
    radiany=float(input("Podaj wartośc kąta w radianach: "))
    stopnie=radiany*180/2*pi
    print(f"Ten kąt ma wartość:{round(stopnie,2)}stopni")

