# es1) ottenere da quattro liste separate una singola lista di dizionari (con "nome", "cognome", "anno di nascita" e "frutto preferito")

utenti_nomi = [
    "Marco", "Luca", "Giulia", "Sara", "Matteo", "Marco", "Francesca", "Elisa", "Davide", 
    "Giulia", "Simone", "Sara", "Andrea", "Marco", "Giorgio", "Luca", "Chiara", "Elisa", 
    "Davide", "Martina", "Marco", "Sara", "Andrea", "Giorgio", "Francesca" 
]

utenti_cognomi = [
    "Rossi", "Bianchi", "Ferrari", "Esposito", "Rossi", "Marchetti", "Romano", "Fontana", 
    "Mancini", "Bianchi", "Conti", "Esposito", "Lombardi", "Rossi", "Barbieri", "Greco", 
    "Fontana", "Romano", "Mancini", "Greco", "Rossi", "Esposito", "Lombardi", "Barbieri", "Ferrari"
]

utenti_anni_nascita = [
    1990, 1985, 1995, 1998, 2000, 1985, 1993, 1987, 1996, 1995, 1999, 1998, 1990, 1985, 1994, 
    2001, 1990, 1987, 1996, 1993, 1985, 1998, 1994, 1987, 1990
]

utenti_frutti_preferiti = [
    "Mela", "Banana", "Fragola", "Arancia", "Mela", "Pera", "Ananas", "Melone", "Pesca", 
    "Fragola", "Uva", "Arancia", "Mango", "Mela", "Limone", "Ciliegia", "Mela", "Kiwi", 
    "Pesca", "Banana", "Melone", "Arancia", "Uva", "Mango", "Pera"
]

# es2) generate un indirizzo email per ogni utente dell'es 1, aggiungendolo al proprio dizionario (campo "email")
# l'indirizzo email é composto da nome_cognome_ultime due cifre dell'anno@gmail.com se sono nati dopo il 1995 e libero.it se sono nati prima
# ES: marco_rossi_90@libero.it   giulia_ferrari_98@gmail.com

# es3) A) usando la comprehension generare la lista di indirizzi email delle persone nate in anni pari 
#      B) usando i filtri e le funzioni lambda generate la lista di indirizzi mail di persone che amano la mela, la pesca o il melone

# es4) prenere le liste di mail dell es 3 , farle diventare set e stampare a video i nomi e i cognomi di:
#      1) chi é nato in anni pari (A) o ama mela, pesca o melone (B)
#      2) chi é nato in anni pari (A) e ama mela, pesca o melone (B)
#      1) chi é nato in anni pari (A) ma non ama mela, pesca o melone (B)

# Dati di esempio
nomi = ['Luca', 'Maria', 'Giovanni']
cognomi = ['Rossi', 'Bianchi', 'Verdi']
anni_nascita = [1990, 1985, 2000]

# Funzione per generare l'email
def genera_email(nome, cognome, anno_nascita):
    # Estrai le ultime due cifre dell'anno
    ultime_due_cifre = str(anno_nascita)[-2:]
    
    # Scegli il dominio in base all'anno di nascita
    if anno_nascita < 1990:
        dominio = 'gmail.com'
    else:
        dominio = 'libero.it'
    
    # Crea l'email unendo nome, cognome e ultime due cifre dell'anno di nascita
    email = f"{nome.lower()}.{cognome.lower()}{ultime_due_cifre}@{dominio}"
    
    return email

# Creare una lista di dizionari con i dati di ciascun individuo
dizionari = [
    {
        'nome': nomi[i],
        'cognome': cognomi[i],
        'anno_nascita': anni_nascita[i],
        'email': genera_email(nomi[i], cognomi[i], anni_nascita[i])
    }
    for i in range(len(nomi))
]

# Stampa i dizionari
for dizionario in dizionari:
    print(dizionario)

#---------------------ESERCIZIO MASSIMO----------------#
    lista_utenti = [
    {
        "nome": utenti_nomi[X],
        "cognome": utenti_cognomi[X],
        "anno_nascita": utenti_anni_nascita[X],
        "frutto_preferito": utenti_frutti_preferiti[X]
    }
    for X in range(len(utenti_nomi))
]
    for utente in lista_utenti:
        nome = utente["nome"].lower()
        cognome = utente["cognome"].lower()
        anno = str(utente["anno_nascita"])[-2:]
        dominio = "@gmail.com" if utente["anno_nascita"] > 1995 else "@libero.it"
        email = f"{nome} {cognome} {anno} {dominio}"
        utente["email"] = email
        print(utente)

