utente = input("Inserisci una lista di numeri separati da spazio: ")

lista = [int(x) for x in utente.split()]


lista_di_dizionari_creata = [
    {"positivo": abs(x), "negativo": -abs(x)} for x in lista
]

print(lista_di_dizionari_creata)
