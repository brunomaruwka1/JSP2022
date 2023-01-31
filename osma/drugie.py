import os

a=os.path.exists('C:\\Users\\bruno\\OneDrive\\Pulpit\\FirstSemester\\python_listy\\osma')
try:
    os.chdir("C:\\Users\\bruno\\OneDrive\\Pulpit\\FirstSemester\\python_listy\\osmy")
    os.mkdir('prywatn')
    print("WESELE")
except FileNotFoundError:
    print("Błąd")
