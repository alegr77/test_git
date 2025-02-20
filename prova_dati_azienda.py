from datetime import datetime
from collections import defaultdict

# Classe per rappresentare un Prodotto
class Prodotto:
    def __init__(self, codice, nome, prezzo):
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo

# Classe per rappresentare un Negozio
class Negozio:
    def __init__(self, nome, paese):
        self.nome = nome
        self.paese = paese

# Classe per rappresentare una Vendita
class Vendita:
    def __init__(self, prodotto, negozio, quantita, data):
        self.prodotto = prodotto
        self.negozio = negozio  # Cambiato 'negocio' con 'negozio'
        self.quantita = quantita
        self.data = data
        self.totale = prodotto.prezzo * quantita

# Classe per gestire le statistiche delle vendite
class StatisticheVendite:
    def __init__(self):
        # Dizionari per memorizzare le vendite
        self.vendite = []
        self.vendite_per_negozio = defaultdict(list)
        self.vendite_per_prodotto = defaultdict(list)
        self.vendite_per_paese = defaultdict(list)

    def aggiungi_vendita(self, vendita):
        self.vendite.append(vendita)
        self.vendite_per_negozio[vendita.negozio].append(vendita)  # Cambiato 'negocio' con 'negozio'
        self.vendite_per_prodotto[vendita.prodotto].append(vendita)
        self.vendite_per_paese[vendita.negozio.paese].append(vendita)  # Cambiato 'negocio' con 'negozio'

    def totale_vendite(self):
        return sum(vendita.totale for vendita in self.vendite)

    def vendite_per_negozio(self):
        res = {}
        for negozio, vendite in self.vendite_per_negozio.items():
            res[negozio.nome] = sum(vendita.totale for vendita in vendite)
        return res

    def vendite_per_prodotto(self):
        res = {}
        for prodotto, vendite in self.vendite_per_prodotto.items():
            res[prodotto.nome] = sum(vendita.totale for vendita in vendite)
        return res

    def vendite_per_paese(self):
        res = {}
        for paese, vendite in self.vendite_per_paese.items():
            res[paese] = sum(vendita.totale for vendita in vendite)
        return res

    def statistiche_vendite(self):
        print(f"Totale vendite: €{self.totale_vendite():.2f}")
        print("Vendite per negozio:")
        for negozio, totale in self.vendite_per_negozio().items():
            print(f"  {negozio}: €{totale:.2f}")
        print("Vendite per prodotto:")
        for prodotto, totale in self.vendite_per_prodotto().items():
            print(f"  {prodotto}: €{totale:.2f}")
        print("Vendite per paese:")
        for paese, totale in self.vendite_per_paese().items():
            print(f"  {paese}: €{totale:.2f}")

# Creazione dei prodotti
prodotto1 = Prodotto(codice="P001", nome="Laptop", prezzo=1000)
prodotto2 = Prodotto(codice="P002", nome="Smartphone", prezzo=600)

# Creazione dei negozi
negozio1 = Negozio(nome="Negozio Roma", paese="Italia")
negozio2 = Negozio(nome="Negozio Milano", paese="Italia")
negozio3 = Negozio(nome="Negozio Parigi", paese="Francia")

# Creazione delle vendite
vendita1 = Vendita(prodotto=prodotto1, negozio=negozio1, quantita=2, data=datetime(2025, 1, 10))
vendita2 = Vendita(prodotto=prodotto2, negozio=negozio1, quantita=3, data=datetime(2025, 1, 12))
vendita3 = Vendita(prodotto=prodotto1, negozio=negozio2, quantita=1, data=datetime(2025, 1, 15))
vendita4 = Vendita(prodotto=prodotto2, negozio=negozio3, quantita=5, data=datetime(2025, 1, 14))

# Creazione delle statistiche di vendita
statistiche = StatisticheVendite()

# Aggiunta delle vendite
statistiche.aggiungi_vendita(vendita1)
statistiche.aggiungi_vendita(vendita2)
statistiche.aggiungi_vendita(vendita3)
statistiche.aggiungi_vendita(vendita4)

# Visualizzazione delle statistiche
statistiche.statistiche_vendite()



