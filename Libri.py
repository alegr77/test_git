# # livello 1
# Creare la classe Libro
# con numero di pagine, titolo, genere, autore, casa editrice, anno di pubblicazione
# # Livello 2
# Aggiungere i controlli su numero di pagine e anno di pubblicazione
# Permettere di inserire libri senza autore e casa editrice (Mettete "Anonimo" e "Nessuna")
# # livello 3
# Creare la classe Libreria che gestisca una serie di libri
# con metodi tipo aggiungi libro, elenca libri per ordine di anno di pubblicazione, elenca libri in ordine alfabetico
# e elenca libri in ordine di autore, elenca libri per numero di pagine

from dataclasses import dataclass, field
from datetime import datetime as dt

@dataclass(unsafe_hash= True)
class Libro:
    titolo :str 
    genere :str = field(repr=False) 
    anno_pubblicazione :int 
    numero_pagine :int
    autore :str = field(default ="Anonimo")
    casa_editrice :str 
    data_inserimento : dt = field(default_factory= lambda: dt.now(), compare=False, hash = False)

    def __repr__(self):
        return f"{self.anno_pubblicazione} - {self.autore} - {self.titolo} ({self.genere})"
    
    @property
    def numero_pagine(self):
        return self._numero_pagine
    
    @numero_pagine.setter
    def numero_pagine(self, value):
        if value <= 0:
            raise ValueError("Il numero di pagine non può essere negativo")
        self._numero_pagine = value

    @property
    def anno_pubblicazione(self):
        return self._anno_pubblicazione
    
    @anno_pubblicazione.setter
    def anno_pubblicazione(self, value):
        if value > dt.now().year:
            raise ValueError("Anno di pubblicazione non valido")
        self._anno_pubblicazione = value

    @property
    def casa_editrice(self):
        return self._casa_editrice

    @casa_editrice.setter
    def casa_editrice(self, value):
        if type(value) in [str, int]:
            self._casa_editrice = value
        else:
            self._casa_editrice = "Nessuna"

@dataclass 
class Libreria:
    elenco_libri: list[Libro] = field(default_factory=lambda: [])  

    def aggiungiLibro(self, libro: Libro):
        self.elenco_libri.append(libro)
    
    def rimuoviLibro(self, libro: Libro):
        self.elenco_libri.remove(libro)
            
    def ordinaLibri(self, criterio: str= "Titolo", reverse :bool = False):

        '''
        questo metodo ordina i libri secondo il parametro criterio passato (di default é "Titolo")
        si puó scegliere tra "Titolo", "Autore", "Pagine" e "Anno"
        mettendo a True il parametro reverse si otterrá l'ordinamento opposto
        '''

        criterio = criterio.upper()
        match criterio:
            case "TITOLO":
                self.elenco_libri.sort(key = lambda x: x.titolo, reverse=reverse)
            case "AUTORE":
                self.elenco_libri.sort(key = lambda x: x.autore, reverse=reverse)
            case "PAGINE":
                self.elenco_libri.sort(key = lambda x: x.numero_pagine, reverse=reverse)
            case "ANNO":
                self.elenco_libri.sort(key = lambda x: x.anno_pubblicazione, reverse=reverse) 

    def stampaLibri(self):
        for libro in self.elenco_libri:
            print(libro)

    def stampaLibriUguali(self, libreria_da_confrontare):
        set_mio = set( (el.titolo, el.autore) for el in self.elenco_libri )
        set_altro = set( (el.titolo, el.autore) for el in libreria_da_confrontare.elenco_libri )
        intersezione_di_libri = set_mio.intersection(set_altro)
        for el in intersezione_di_libri:
            print(el)

    def generePiuDiffuso(self):
        elenco_generi = {}
        for libro in self.elenco_libri:
            if libro.genere not in elenco_generi:
                elenco_generi[libro.genere] = 0
            elenco_generi[libro.genere] += 1
        elenco_generi = dict(sorted(elenco_generi.items(), key=lambda x: x[1], reverse=True))
        return list(elenco_generi)[0]
    
    @classmethod
    def metodoDiClasseStampaLibriUguali(cls, libreria_da_confrontare1, libreria_da_confrontare2):
        set_1 = set( (el.titolo, el.autore) for el in libreria_da_confrontare1.elenco_libri )
        set_2 = set( (el.titolo, el.autore) for el in libreria_da_confrontare2.elenco_libri )
        intersezione_di_libri = set_1.intersection(set_2)
        for el in intersezione_di_libri:
            print(el)
    
    @classmethod
    def classificaGeneriContenutiInLibrerie(cls, *librerie):
        elenco_generi = {}
        for libreria in librerie:
            for libro in libreria.elenco_libri:
                if libro.genere not in elenco_generi:
                    elenco_generi[libro.genere] = 0
                elenco_generi[libro.genere] += 1
        elenco_generi = dict(sorted(elenco_generi.items(), key=lambda x: x[1], reverse=True))
        return elenco_generi
    
dataset_libri = [
    Libro(autore="Alice Oseman", titolo="Nick and Charlie", genere="Novel", numero_pagine=200, casa_editrice="Harper Collins", anno_pubblicazione=2020),
    Libro(autore="J.K. Rowling", titolo="Harry Potter e la pietra filosofale", genere="Fantasy", numero_pagine=320, casa_editrice="Salani", anno_pubblicazione=1997),
    Libro(autore="George Orwell", titolo="1984", genere="Dystopian", numero_pagine=328, casa_editrice="Mondadori", anno_pubblicazione=1949),
    Libro(autore="J.R.R. Tolkien", titolo="Il Signore degli Anelli", genere="Fantasy", numero_pagine=1200, casa_editrice="Bompiani", anno_pubblicazione=1954),
    Libro(autore="Francesco Gabbani", titolo="Le Vie del Circo", genere="Autobiografia", numero_pagine=256, casa_editrice="Rizzoli", anno_pubblicazione=2023),
    Libro(autore="Markus Zusak", titolo="La ladra di libri", genere="Historical Fiction", numero_pagine=550, casa_editrice="Frassinelli", anno_pubblicazione=2005),
    Libro(autore="Harper Lee", titolo="To Kill a Mockingbird", genere="Classic", numero_pagine=281, casa_editrice="J.B. Lippincott & Co.", anno_pubblicazione=1960),
    Libro(autore="F. Scott Fitzgerald", titolo="Il grande Gatsby", genere="Classic", numero_pagine=180, casa_editrice="Scribner", anno_pubblicazione=1925),
    Libro(autore="Paulo Coelho", titolo="L'alchimista", genere="Adventure", numero_pagine=190, casa_editrice="HarperOne", anno_pubblicazione=1988),
    Libro(autore="Stephen King", titolo="It", genere="Horror", numero_pagine=1138, casa_editrice="Viking Penguin", anno_pubblicazione=1986),
    Libro(autore="Dan Brown", titolo="Il codice da Vinci", genere="Thriller", numero_pagine=689, casa_editrice="Doubleday", anno_pubblicazione=2003),
    Libro(autore="Jane Austen", titolo="Orgoglio e pregiudizio", genere="Romance", numero_pagine=432, casa_editrice="T. Egerton", anno_pubblicazione=1813),
    Libro(autore="Leo Tolstoy", titolo="Anna Karenina", genere="Classic", numero_pagine=864, casa_editrice="The Russian Messenger", anno_pubblicazione=1878),
    Libro(autore="Gabriel García Márquez", titolo="Cent'anni di solitudine", genere="Magical realism", numero_pagine=417, casa_editrice="Editorial Sudamericana", anno_pubblicazione=1967),
    Libro(autore="Isaac Asimov", titolo="Fondazione", genere="Science Fiction", numero_pagine=255, casa_editrice="Gnome Press", anno_pubblicazione=1951),
    Libro(autore="Khaled Hosseini", titolo="Il cacciatore di aquiloni", genere="Historical Fiction", numero_pagine=371, casa_editrice="Riverhead Books", anno_pubblicazione=2003),
    Libro(autore="Margaret Atwood", titolo="Il racconto dell'ancella", genere="Dystopian", numero_pagine=311, casa_editrice="McClelland & Stewart", anno_pubblicazione=1985),
    Libro(autore="Arthur Conan Doyle", titolo="Sherlock Holmes - Il mastino dei Baskerville", genere="Mystery", numero_pagine=256, casa_editrice="George Newnes", anno_pubblicazione=1902),
    Libro(autore="Suzanne Collins", titolo="Hunger Games", genere="Dystopian", numero_pagine=374, casa_editrice="Scholastic Press", anno_pubblicazione=2008),
    Libro(autore="J.R.R. Tolkien", titolo="Lo Hobbit", genere="Fantasy", numero_pagine=310, casa_editrice="George Allen & Unwin", anno_pubblicazione=1937),
    Libro(autore="Haruki Murakami", titolo="Norwegian Wood", genere="Romance", numero_pagine=296, casa_editrice="Kodansha", anno_pubblicazione=1987),
    Libro(autore="Neil Gaiman", titolo="American Gods", genere="Fantasy", numero_pagine=465, casa_editrice="Harcourt", anno_pubblicazione=2001),
    Libro(autore="Chimamanda Ngozi Adichie", titolo="Mezzo sole giallo", genere="Historical Fiction", numero_pagine=448, casa_editrice="Knopf", anno_pubblicazione=2006),
    Libro(autore="Toni Morrison", titolo="Beloved", genere="Historical Fiction", numero_pagine=324, casa_editrice="Alfred A. Knopf", anno_pubblicazione=1987),
    Libro(autore="Yuval Noah Harari", titolo="Sapiens. Da animali a dèi", genere="Non-fiction", numero_pagine=464, casa_editrice="Harvill Secker", anno_pubblicazione=2011),
    Libro(autore="Colleen Hoover", titolo="It Ends with Us", genere="Romance", numero_pagine=384, casa_editrice="Atria Books", anno_pubblicazione=2016),
    Libro(autore="Ernest Hemingway", titolo="Il vecchio e il mare", genere="Classic", numero_pagine=128, casa_editrice="Charles Scribner's Sons", anno_pubblicazione=1952),
    Libro(autore="John Green", titolo="Colpa delle stelle", genere="Young Adult", numero_pagine=313, casa_editrice="Dutton Books", anno_pubblicazione=2012),
    Libro(autore="C.S. Lewis", titolo="Le cronache di Narnia", genere="Fantasy", numero_pagine=766, casa_editrice="Geoffrey Bles", anno_pubblicazione=1950),
    Libro(autore="E.L. James", titolo="Cinquanta sfumature di grigio", genere="Romance", numero_pagine=514, casa_editrice="Vintage Books", anno_pubblicazione=2009),
    Libro(autore="Douglas Adams", titolo="Guida galattica per autostoppisti", genere="Science Fiction", numero_pagine=224, casa_editrice="Pan Books", anno_pubblicazione=1979),
    Libro(autore="Albert Camus", titolo="Lo straniero", genere="Philosophical", numero_pagine=123, casa_editrice="Gallimard", anno_pubblicazione=1942),
    Libro(autore="Bram Stoker", titolo="Dracula", genere="Horror", numero_pagine=418, casa_editrice="Archibald Constable and Company", anno_pubblicazione=1897),
    Libro(autore="Ray Bradbury", titolo="Fahrenheit 451", genere="Dystopian", numero_pagine=256, casa_editrice="Ballantine Books", anno_pubblicazione=1953)
]

