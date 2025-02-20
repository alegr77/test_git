stringa_utente = input("Inserisci una frase")
separatore = input("Quale separatore hai usato?")
lista_con_separatore = stringa_utente.split(separatore)
lista_con_separatore.sort()
print(f"La lista è ordinata {lista_con_separatore}")

