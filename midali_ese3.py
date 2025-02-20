while True:
    risposta = input("Vuoi inserire una lista di numeri o hai finito? Digita \"A\" per continuare o \"ho finito\"").lower()
    if risposta == "ho finito":
        print("Programma finito")
        break
if risposta == "A":
    lista =[]
    numeri = int(input("Quanti numeri vuoi inserire?"))
    i = 0
    while i < numeri:
        num = int(input("Inserisci un numero: "))
        lista.append(num)
        i += 1
    somma = 0
    i = 0
    while i < len(lista):
        somma += lista[i]
        i += 1
    print(f"La somma di tutti i numeri inseriti è {somma}")
else:
    print("Per favore digita \"A\" per continuare oppure \"ho finito\" per interrompere il programma")


    
     
   
          

#     numero = input("Inserisci un numero (oppure 'ho finito' per interrompere)").lower()

#     if numero == "ho finito":
#         print("Programma interrotto")
#         break
#     numero = int(numero)
#     if numero < 0:
#             print("Errore! Inserisci numero positivo")
#     elif numero >= 0:
         

