while True:
    nome = input("Inserisci un nome:")
    if nome != "Thomas":
         print ("Username non trovato")
         continue
    password = input ("Inserisci la password: ")
    if password == "paperino":
         break
    print ("Password sbagliata!")
         

