print("Registra la tua lista di persone")
lista = []
while True:
     dizionario = {
     "nome":0,
     "cognome": 0,
     #"anno_nascita":0,
     #"bibita_prefe":0,
     }
     for chiave in dizionario.keys():
          print(f"Inserisci {chiave}")
          dizionario[chiave]=input()
     lista.append(dizionario)
     scelta=input("Vuoi continuare?")
     if scelta == "si":
          continue
     else:
          break
#print(lista)

lista_ordinata = []
for el in lista:
     lista_ordinata.append(el["nome"])
     lista_ordinata.sort()
print(f"{lista_ordinata =}")

lista_ordinata_2 = []
for el in lista:
     lista_ordinata_2.append(el["cognome"])
     lista_ordinata_2.sort()
     
print(f"{lista_ordinata_2 = }")



