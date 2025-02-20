#numero=int(input())
#print("Inserisci un numero") equivale a:

numero = int(input("Inserisci un numero"))
somma = numero

while numero != 0:
    numero = int(input("Inserisci un numero"))
    somma += numero
    print(f"La somma è {somma}")

print("Programma finito")   