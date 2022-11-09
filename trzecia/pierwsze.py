x=str(input("Podaj litere a ja Ci powiem czy to samogloska czy spolgloska: "))
if len(x)==1:
    if x in "aeiouyąęó":
        print("To jest samogłoska")
    else:
        print("To jest spółgłoska")
else:
    print("To nie jest spółgłoska ani samogłoska.")
    