numero = int(input("Inserisci un numero"))
risultato = 1
for i in range (1,numero+1,1):
    risultato = risultato * i 

print(f"Il fattoriale di questo numero è  {risultato}")