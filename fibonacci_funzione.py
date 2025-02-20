def nFibonacci(posizione):
    addendo1 = 0
    addendo2 = 1
    for i in range(1, posizione):
        somma = addendo1 + addendo2
        addendo2 = addendo1
        addendo1 = somma

    return somma

corrispondenza = int(input("Inserisci la posizione di cui vuoi sapere il numero di Fibonacci corrispondente: "))

risultato = nFibonacci(corrispondenza)
print(f"Il numero di Fibonacci in posizione {corrispondenza} è {risultato}")


    
