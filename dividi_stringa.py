frase = input("Inserisci una frase")
separatore = input("Come hai separato le parole tra loro?")
lista = []
ho_finito = False

while not ho_finito:
    indice_dove_trovo_separatore = frase.find(separatore)
    if indice_dove_trovo_separatore == -1:
        parola = frase [:]
        ho_finito = True
    else:
        parola = frase [:indice_dove_trovo_separatore]
        lista.append(parola)
        frase = frase[indice_dove_trovo_separatore + len(separatore):]

print(lista) 
#???? non funziona