numero = 0
lista = []
massimo = 0
temp = 0
while numero < 10:
    num_utente = int(input("Inserisci un valore"))
    lista.append(num_utente)
    numero += 1
for i in range(10):
    for j in range (10-i-1):
        massimo = lista[j]
        if lista[j]>lista[j+1]:
             temp = lista[j+1]
             lista[j+1]=lista[j]
             lista[j]=temp  

#temp = lista[i+1]
#lista[i+1]=lista[i]
#lista[i]=temp
print(lista)

