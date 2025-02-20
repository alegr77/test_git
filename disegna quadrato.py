lato = int(input("Inserisci un lato del quadrato: "))
while lato <= 1 :
     print ("Errore! Inserisci un numero maggiore di 1")
     lato = int(input("Inserisci un lato del quadrato: "))

print("Con che carattere vuoi che venga fatto il quadrato?")
carattere = input()
contatore_linea = 1
contatore_carattere = 1

for contatore_linea in range(contatore_linea, lato+1, 1):
     contatore_linea = contatore_linea + 1
     print(lato*carattere)

#lato = int(input("Inserisci il lato del quadrato"))
#for i in range(0, lato, 1):
     #for j in range(0, lato, 1):
     #print("*", end= "")
     #print("")

#range(lato) => range(0, lato, 1)


