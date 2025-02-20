while True:
    numero = input("Inserisci un numero (oppure 'ho finito' per interrompere)").lower()

    if numero == "ho finito":
        print("Programma interrotto")
        break
    numero = int(numero)
    if numero < 0:
            print("Errore! Inserisci numero positivo")
    elif numero >= 0:
         
        #  while numero <= 0:
        #       print(numero)
        #       numero -= 1
        #       continue
        
        for i in range(numero, -1, -1):
            print(i)
            numero -= 1





   

    

            






