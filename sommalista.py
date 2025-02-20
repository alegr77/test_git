lista = []
somma = 0
prodotto = 1
numero = input("Inserisci un numero")
while numero != ("finito").upper():
    if numero == "finito":
        break
    else: 
        lista.append(int(numero))
        numero =input("Inserisci un numero")
for i in range(len(lista)):
       somma += lista[i]
    prodotto = lista[i]*prodotto
print(f"La somma dei numeri è {somma}")
print(f"Il prodotto dei numeri è {prodotto}")


