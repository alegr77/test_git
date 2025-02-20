while True:
    lato1 = int(input("Inserisci lato 1:"))
    lato2 = int(input("Inserisci lato 2:"))
    lato3 = int(input("Inserisci lato 3:"))

    if lato1 < 0:
        print("Errore! Lato1 è minore di 0; mettilo positivo!")
        continue
    if lato2 < 0:
        print("Errore! Lato2 è minore di 0; mettilo positivo!")
        continue
    if lato3 < 0:
        print("Errore! Lato3 è minore di 0; mettilo positivo!")
        continue
    if lato1 + lato2 < lato3:
        print("Errore! La somma di lato1 e lato2 è minore di lato 3.")
        continue
    if lato1 + lato3 < lato2:
        print("Errore! La somma di lato1 e lato3 è minore di lato 2.")
        continue
    if lato2 + lato3 < lato1:
         print("Errore! La somma di lato2 e lato 3 è minore di lato1")
         continue
    break
print("Bravo")
