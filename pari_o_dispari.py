def isEven(number :int):
    if number%2 == 0:
        return True
    return False

n = int(input("Inserisci un numero: "))
if isEven(n):
    print("È pari")
else:
    print("È dispari")