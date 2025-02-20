lista_numeri_utente = []
somma = 0
prodotto = 1
risposta_utente = input("Inserisci un numero e scrivi HO FINITO quando hai finito")
while risposta_utente != "HO FINITO":
    lista_numeri_utente.append(int(risposta_utente))
    risposta_utente = input("Inserisci un numero e scrivi HO FINITO quando hai finito")
for el in lista_numeri_utente:
    somma += el
media = somma/len(lista_numeri_utente)
print(f"La media di questi numeri è {media}")

somma1 = 0
for el in lista_numeri_utente:
     somma1 += ((el-media)**2)
     varianza = somma1/len(lista_numeri_utente)
print(f"La varianza di questa lista è {varianza}")






