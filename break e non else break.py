while True:
    lato1 = int(input("Inserisci lato1: "))
    lato2 = int(input("Inserisci lato2: "))
    lato3 = int(input("Inserisci lato3: "))
    if lato1>0 and lato2>0 and lato3>0:
        perimetro = lato1 + lato2 + lato3
        print(f"Il perimetro è {perimetro}")
        break
    print("Il programma è finito")