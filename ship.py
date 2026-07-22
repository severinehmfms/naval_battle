from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Ship:
    name: str
    length_ship: int
    sens: str
    first_case: str
    nb_touche: int
    is_coule: bool
    list_cases: list[str]
    ships_list: ClassVar[list['Ship']] = []

    def __init__(self, name, length_ship, sens, first_case):
        """  Méthode pour instancier un nouveau navire 
                paramètres attendus :
                name = Nom du navire
                length_ship = Taille du navire
                sens = Sens du navire H/V
                firs_case = Première case du navire
             """
        self.name = name
        self.length_ship = length_ship
        self.sens = sens
        self.first_case = first_case
        self.nb_touche = 0
        self.is_coule = False
        self.list_cases = []
        #On ajoute le navire à la liste des navires
        Ship.ships_list.append(self)

    def set_list_cases(self, list_cases):
        """Méthode pour mettre à jour la liste des cases du navire"""
        self.list_cases = list_cases

    @staticmethod
    def get_list_ships():
        """ Fonction qui renvoie la liste des navires"""
        return Ship.ships_list