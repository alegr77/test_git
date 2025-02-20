#Creare una funzione che dati tre valori naturali,
#se tra questi c’è (almeno) una coppia, restituisce il valore del numero ripetuto, 
#altrimenti restituisce -1.

def naturali (n1, n2, n3):
    if n1 == n2:
        return n1
    elif n1 == n3:
        return n1
    elif n2 == n3:
        return n2
    else:
        return -1
    
def confronto_naturali(tripletta1, tripletta2):
    coppia1 = naturali(tripletta1[0], tripletta1[1], tripletta1[2])
    coppia2 = naturali(tripletta2[0], tripletta2[1], tripletta2[2])

    if coppia1 == -1 and coppia2 == -1:
         return "Non ci sono coppie di numeri uguali tra loro"
    elif coppia1 == -1:
        return f"La coppia di numeri maggiore è: {coppia2}"
    elif coppia2 == -1:
        return f"La coppia di numeri maggiore è: {coppia1}"
    else:
        return f"La coppia più alta tra le due triplette è: {max(coppia1, coppia2)}"
    
tripletta1 = [int(x) for x in input("Inserisci la prima tripletta di numeri separati da uno spazio: ").split()]
tripletta2 = [int(x) for x in input("Inserisci la seconda tripletta di numeri separati da uno spazio: ").split()]
    
print(confronto_naturali(tripletta1, tripletta2))
    
    
    






