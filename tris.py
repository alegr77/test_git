tabellone = [[" " for _ in range (3)] for _ in range(3)]
def crea_griglia(tabellone):
        for riga in tabellone:
                print("|".join(riga))
                print("-"*5)

print(crea_griglia(tabellone))

utente1 = "X"
utente2 = "O"
for riga in tabellone:
        if riga[0] == riga[1] == riga[2] == utente1:
                print("Ha vinto utente 1")
        elif riga[0] == riga[1] == riga[2] == utente2: 
                print("Ha vinto utente 2")
        else:
             break
for riga1 in tabellone:
        if riga1[0] == riga1[1] == riga1[2] == utente1:
                print("Ha vinto utente 1")
        elif riga1[0] == riga1[1] == riga1[2] == utente2: 
                print("Ha vinto utente 2")
        else:
            break
for riga2 in tabellone:
        if riga2[0] == riga2[1] == riga2[2] == utente1:
                print("Ha vinto utente 1")
        elif riga2[0] == riga2[1] == riga2[2] == utente2: 
                print("Ha vinto utente 2")
        else:
            break
for colonna in tabellone:
        if riga[0] == riga1[0] == riga2[0] == utente1:
                print("Ha vinto utente 1")
        elif riga[0] == riga1[0] == riga2[0] == utente2:
                print("Ha vinto utente 2")
        else:
            break
for colonna1 in tabellone:
        if riga[1] == riga1[1] == riga2[1] == utente1:
                print("Ha vinto utente 1")
        elif riga[1] == riga1[1] == riga2[1] == utente2:
                print("Ha vinto utente 2")
        else:
            break
for colonna2 in tabellone:
        if riga[2] == riga1[2] == riga2[2] == utente1:
                print("Ha vinto utente 1")
        elif riga[2] == riga1[2] == riga2[2] == utente2:
                print("Ha vinto utente 2")
        else:
            break
for diagonale1 in tabellone:
        if riga[0] == riga1[1] == riga2[2] == utente1:
                print("Ha vinto utente 1")
        elif riga[0] == riga1[1] == riga2[2] == utente2:
                print("Ha vinto utente 2")
        else:
            break
for diagonale2 in tabellone:
        if riga[2] == riga1[1] == riga2[0] == utente1:
                print("Ha vinto utente 1")
        elif riga[2] == riga1[1] == riga2[0] == utente2:
                print("Ha vinto utente 2")
        else:
            break



while True:
    riga = int(input("Inserisci il numero della riga (compreso tra 0 e 2)"))
    colonna = int(input("Inserisci il numero della colonna (compreso tra 0 e 2)"))
    if riga < 0 or riga > 2 or colonna < 0 or colonna > 2:
        print("Errore! Inserisci numero tra 0 e 2!!!")
        continue
    if tabellone[riga][colonna] == " ":
        simbolo = input("Inserisci simbolo (X oppure O): ")
        tabellone[riga][colonna] = simbolo
        break
    else:
        print("È occupato")
    
            

        


                
