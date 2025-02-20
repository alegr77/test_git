from dataclasses import dataclass
from typing import List
from figure import Rettangolo
from classi3 import Cerchio

@dataclass
class PianoCartesiano:
    figure_geometriche : List
    def aggiungi_Cerchio(self, cerchio_da_aggiungere):
        if isinstance(cerchio_da_aggiungere, Cerchio):
            self.figure_geometriche.append(cerchio_da_aggiungere)
        else:
            print("Errore! Non hai aggiunto un cerchio")
    def aggiungi_Rettangolo(self, rettangolo_da_aggiungere):
        if isinstance(rettangolo_da_aggiungere, Rettangolo):
            self.figure_geometriche.append(rettangolo_da_aggiungere)
        else:
            print("Errore! Non hai aggiunto un rettangolo")
    def elenca_tutto(self):
        for el in self.figure_geometriche:
            print(el)

mio_piano_cartesiano = PianoCartesiano(figure_geometriche=[])
ret1 = Rettangolo(v1_x=1, v1_y=2, v2_x=3, v2_y=4)
cerchio1 = Cerchio(x_centro=1, y_centro=2, raggio=3)
cerchio2 = Cerchio(x_centro=5, y_centro=3, raggio=4)
mio_piano_cartesiano.aggiungi_Rettangolo(ret1)
mio_piano_cartesiano.aggiungi_Cerchio(cerchio1)
mio_piano_cartesiano.aggiungi_Cerchio(cerchio2)