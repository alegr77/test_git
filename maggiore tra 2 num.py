print("Inserisci il primo numero")
numero1 = int(input())

print("Inserisci il secondo numero")
numero2 = int(input())

if numero1 > numero2:
    print(f"Il numero maggiore è: {numero1}")
elif numero2 > numero1:
    print(f"Il numero maggiore è: {numero2}")
else:
    print("I due numeri sono uguali")
