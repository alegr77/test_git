# Creare una classe Persona con nome, cognome, anno di nascita e anni
# creare due costruttori, uno che accetti  nome, cognome e anno di nascita 
# e l'altro che accetti nome, cognome e anni

from dataclasses import dataclass
import datetime

@dataclass
class Persona:
    nome:str
    cognome:str
    _anno_di_nascita:int
    _anni:int
    _genere :str

    def __init__(self, nome :str, cognome :str, anno_di_nascita:int, anni :int, genere :str):
        self.nome = nome
        self.cognome = cognome
        self.anno_di_nascita = anno_di_nascita
        self.anni = anni
        self.genere = genere

    def __repr__(self):
        if self.genere == "F":
            return f"Ragazza ({self.nome}, {self.cognome})"
        if self.genere == "M":
            return f"Ragazzo ({self.nome}, {self.cognome}, {self.anno_di_nascita}, {self.anni} anni)"
        return f"Persona ({self.nome}, {self.cognome}, {self.anno_di_nascita}, {self.anni} anni)"

    @classmethod
    def personaDatoAnnoDiNascita(cls, nome, cognome, anno_di_nascita, genere):
        anni = datetime.datetime.now().year - anno_di_nascita
        return cls(nome = nome, cognome = cognome, anno_di_nascita = anno_di_nascita, anni = anni, genere = genere)

    @classmethod
    def personaDatiAnni(cls, nome, cognome, anni, genere):
        anno_di_nascita = datetime.datetime.now().year - anni
        return cls(nome = nome, cognome = cognome, anno_di_nascita = anno_di_nascita, anni = anni, genere = genere)

    @property
    def anni(self):
        if self._genere == "F":
            raise Exception ("Errore, non si chiede l'etá a una ragazza")
        return self._anni

    @anni.setter
    def anni(self, valore):
        if valore < 0:
            raise Exception("Anni non può essere negativo")
        self._anni = valore

    @property
    def anno_di_nascita(self):
        if self._genere == "F":
            raise Exception("Errore, non si chiede l'etá a una ragazza")
        return self._anno_di_nascita
        
    @anno_di_nascita.setter
    def anno_di_nascita(self, valore):
        if valore > datetime.datetime.now().year:
            raise Exception("Anno di nascita non può essere nel futuro")
        self._anno_di_nascita = valore

    @property
    def genere(self):
        return self._genere
        
    @genere.setter
    def genere(self, valore :str):
        valore = valore.upper()
        if valore not in ["M", "F", "*"]:
            raise Exception("Genere non valido")
        self._genere = valore

persona1 = Persona.personaDatoAnnoDiNascita(nome="Thomas", cognome="Naccari", anno_di_nascita=1998, genere="M")
persona2 = Persona.personaDatoAnnoDiNascita(nome="Elly", cognome="Silly", anno_di_nascita=2002, genere="F")

print(persona1)
print(persona2)



    
