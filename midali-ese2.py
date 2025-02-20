while True:

    numero = input("Inserisci un numero (oppure \"ho finito\" per interrompere il programma): ").lower()

    if numero == "ho finito":
        print("Programma interrotto")
        break
    numero = int(numero)
    fattoriale=1
    i=1
    if numero < 0:
            print("Errore! Inserisci numero positivo")
            break
    elif numero >= 0:
         while i <= numero:
              fattoriale *= i
              i += 1

    print(f"Il fattoriale di questo numero è {fattoriale}")

              