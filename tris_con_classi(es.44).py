from dataclasses import dataclass, field
import os

@dataclass 
class Campo:
    campo: list 

    def __init__(self):
        self.campo = [" ", " ", " "," ", " ", " "," ", " ", " "]
    
    def stampa_campo(self):
        print("    A    B     C")
        print(f"1   {self.campo[0]} |  {self.campo[3]}  |  {self.campo[6]}")
        print("  ---------------")
        print(f"2   {self.campo[1]} |  {self.campo[4]}  |  {self.campo[7]}")
        print("  ---------------")
        print(f"3   {self.campo[2]} |  {self.campo[5]}  |  {self.campo[8]}")

    def indice_da_coordinate(self, coordinata):
        coordinata = coordinata.upper()
        mappa_coordinate = {"A1": 0, "A2":1, "A3":2,
                             "B1": 3, "B2": 4, "B3": 5,
                             "C1": 6, "C2": 7, "C3": 8
                            }
        return mappa_coordinate.get(coordinata, -1)

    def inserisci_valore(self, coordinata, simbolo):
        indice = self.indice_da_coordinate(coordinata)
        if indice == -1:
            return ("La coordinata in cui hai inserito il simbolo non esiste.")
        if self.campo[indice] == " ":
            self.campo[indice] = simbolo
            return True
        return self.campo[indice]
    
    def controlla_tre_valori(self, valore1, valore2, valore3):
        return valore1 == valore2 == valore3 and valore1 != " "
    
    def stato_del_gioco(self):
        #CONTROLLO LE RIGHE
        if self.controlla_tre_valori(self.campo[0], self.campo[1], self.campo[2]):
            return self.campo[0]
        if self.controlla_tre_valori(self.campo[3], self.campo[4], self.campo[5]):
            return self.campo[3]
        if self.controlla_tre_valori(self.campo[6], self.campo[7], self.campo[8]):
            return self.campo[6]
        #CONTROLLO LE COLONNE
        if self.controlla_tre_valori(self.campo[0], self.campo[3], self.campo[6]):
            return self.campo[0]
        if self.controlla_tre_valori(self.campo[1], self.campo[4], self.campo[7]):
            return self.campo[1]
        if self.controlla_tre_valori(self.campo[2], self.campo[5], self.campo[8]):
            return self.campo[2]
        #CONTROLLO LE DIAGONALI
        if self.controlla_tre_valori(self.campo[0], self.campo[4], self.campo[8]):
            return self.campo[0]
        if self.controlla_tre_valori(self.campo[2], self.campo[4], self.campo[6]):
            return self.campo[2]
        #CONTROLLO SE SI PUÓ CONTINUARE A GIOCARE
        for el in self.campo:
            if el == " ":
                return True
        return "="
class Partita:
    def __init__(self, nome_G1, nome_G2):
        self.campo = Campo()
        self.nomeG1 = nome_G1
        self.nomeG2 = nome_G2
        self.simboloG1 = "X"
        self.simboloG2 = "O"
        self.turno = self.simboloG1
        self.vittorieG1 = 0
        self.vittorieG2 = 0

    def gioca(self):
        while True:
            while self.campo.stato_del_gioco() == True:
                os.system("clear")
                self.campo.stampa_campo()

                while True:
                    if self.turno == self.simboloG1:
                        nome_giocatore = self.nomeG1
                    else:
                        nome_giocatore = self.nomeG2

                    coordinata = input(f"{nome_giocatore}, dove vuoi mettere la {self.turno}?").upper()
                    risultato = self.campo.inserisci_valore(coordinata, self.turno)

                    if risultato == True:
                        break
                    elif risultato == "Non valido":
                        print(f"Errore: La coordinata {coordinata} non esiste, usa il formato corretto (es. A2)")
                    else:
                        print(f"Errore!!! La cella {coordinata} è gia occupata da {risultato}")
            #CONTROLLO SE HA VINTO QUALCUNO
                risultato_partita = self.campo.stato_del_gioco()
                if risultato_partita != True:
                    os.system("clear")
                    self.campo.stampa_campo()
                    if risultato_partita == "=":
                        print("Pareggio! Ha vinto lo sport")
                    else:
                        if risultato_partita == self.simboloG1:
                            print(f"Ebbravo {self.nomeG1}! Hai vinto tu!")
                            self.vittorieG1 +=1
                        else:
                            print(f"Ebbravo {self.nomeG2}! Hai vinto tu!")
                            self.vittorieG2 += 1
                    break
                #CAMBIO IL TURNO
                if self.turno == self.simboloG1:
                    self.turno = self.simboloG2
                else:
                    self.turno = self.simboloG1

            print(f" Punteggio attuale: {self.nomeG1} {self.vittorieG1} - {self.nomeG2} {self.vittorieG2}")
            risposta = input("Volete giocare un'altra partita?").lower()
            if risposta != "si":
                print("Grazie per aver giocato")
                break
            else:
                self.campo = Campo()
                self.turno = self.simboloG1
             
if __name__ == "__main__":
    nome_G1 = input("Inserisci il nome del primo giocatore (X): ")
    nome_G2 = input("Inserisci il nome del secondo giocatore (O): ")
    partita = Partita(nome_G1, nome_G2)
    partita.gioca()


                                
#campo = Campo()
#campo.stampa_campo()
