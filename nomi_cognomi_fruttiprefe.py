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

lista_mista = [
            {
                "nome":nome,
                "cognome":cognome,
                "anno di nascita":anno,
                "frutto prefe":frutto,
            
            } 
            for nome,cognome,anno,frutto in zip(utenti_nomi, utenti_cognomi, utenti_anni_nascita,utenti_frutti_preferiti)]
print(lista_mista)

for elemento in lista_mista:
    nome=elemento['nome'].lower()
    cognome=elemento['cognome'].lower()
    anno=str(elemento['anno di nascita'])[-2:]
    dominio='@gmail.com' if elemento['anno di nascita']>1995 else '@libero.it'
    email=f"{nome}_{cognome}_{anno}{dominio}"
    elemento['email']=email

    print(email)
set_nomi_utenti_anniPari= {el['nome']+' '+ el['cognome'] for el in lista_mista if el['anno di nascita']%2==0}

lista_mail_annoPari=[el['email']for el in lista_mista if el['anno di nascita']%2==0]

set_1 = set(lista_mail_annoPari)
print(set_1)
lista_nomi_utenti_frutti = list(filter(lambda el: el ["frutto prefe"] == "Mela" or el["frutto prefe"] == "Melone" or el["frutto prefe"] == "Pesca", lista_mista))
print(lista_nomi_utenti_frutti)

email_utenti_frutti_selezionati = list(map(lambda el: el["email"], lista_nomi_utenti_frutti))
print(email_utenti_frutti_selezionati)
set_2 = set(email_utenti_frutti_selezionati)
print(set_2)

set_4 = set_1.union(set_2)
print(set_4)
set_5 = set_1.intersection(set_2)
print(set_5)
set_6 = set_1.difference(set_2)
print(set_6)

# utenti = []
# for nome, cognome, anno, frutto in list(zip(utenti_nomi, utenti_cognomi, utenti_anni_nascita, utenti_frutti_preferiti)):
#     utenti.append({"nome": nome,
#                    "cognome": cognome,
#                    "anno": anno,
#                    "frutto": frutto})
    
# utenti_mela_pesca_melone = list(filter(lambda el: el["frutto"] == "Mela" or el["frutto"] == "Pesca" or el["frutto"] == "Melone", utenti))
# email_utenti_mela_pesca_melone = list(map(lambda el: el["nome"], utenti_mela_pesca_melone))

# print(email_utenti_mela_pesca_melone)