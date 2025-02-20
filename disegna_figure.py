figura = input("Che figura vuoi disegnare? Quadrato, Rettangolo o Triangolo?").upper()
carattere = input("Di che carattere vuoi che sia composta la figura? (Inserisci un solo carattere)")
if len(carattere) != 1:
    print("Errore! Inserisci un solo carattere")
    exit()
match figura:
    case "QUADRATO" | "Q":
        lato = int(input("Inserisci il lato del quadrato"))
        for i in range(lato):
                print(carattere*lato)
    case "RETTANGOLO" | "R":
        base = int(input("Inserisci la base del rettangolo"))
        altezza = int(input("Inserisci l'altezza del rettangolo"))
        for i in range (altezza):
            print(carattere*base)
    case "TRIANGOLO" | "T":
        altezza = int(input("Inserisci l'altezza del triangolo"))
        for i in range (altezza):
            numero_spazi = altezza - i - 1
            numero_carattere = i * 2 + 1
            for j in range (numero_spazi):
                print (" ", end ="")
            for j in range (numero_carattere):
                print("*", end = "")
            print()
    case _:
            print("Figura non riconosciuta")


