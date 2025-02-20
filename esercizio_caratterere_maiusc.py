def conta_maiuscole (carattere1, carattere2, carattere3):
    contatore = 0

    if carattere1.isupper():
        contatore += 1
    if carattere2.isupper():
        contatore += 1
    if carattere3.isupper():
        contatore += 1
    return contatore

c1 = input("Inserisci il primo carattere: ")
c2 = input("Inserisci il secondo carattere: ")
c3 = input("Inserisci il terzo carattere: ")


numero_maiuscole = conta_maiuscole (c1, c2, c3)
print(f"Il numero di maiuscole è: {numero_maiuscole}")


