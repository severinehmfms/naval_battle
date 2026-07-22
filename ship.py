from dataclasses import dataclass
from typing import ClassVar
import constantes as const

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

    def get_case_suivante(self, case, sens):
        """ Fonction qui va renvoyer les coordonnées de la case suivante en fonction du sens"""
        # On décompose la case entre lettre_colonne et numero_ligne
        lettre_colonne = case[0]
        numero_ligne = case[1:2]
        case_suivante = ""
        if sens == const.CONST_HORIZONTAL:
            # Nouvelle case = colonne + 1, même numéro de ligne
            indice_colonne = const.columns_alpha_list.index(lettre_colonne)
            case_suivante = const.columns_alpha_list[indice_colonne + 1].upper() + str(numero_ligne)
        elif sens == const.CONST_VERTICAL:
            # Nouvelle case = même colonne, numéro de ligne + 1
            case_suivante = lettre_colonne.upper() + str(int(numero_ligne) + 1)
        return case_suivante

    def get_list_cases(self):
        """
            Fonction qui retourne les coordonnées des cases qui composent un navire (sous forme de tableau)
            firt_case : Coordonnées de la première case
            sens : Sens du bateau horizontal ou vertical H/V
            length_ship : la taille du bateau

        """
        list_cases = [self.first_case]
        case_en_cours = self.first_case
        # Pour la longueur du navire je rajoute les cases
        for _ in range(1, self.length_ship):
            case_en_cours = self.get_case_suivante(case_en_cours, self.sens)
            list_cases.append(case_en_cours)
        return list_cases

    def touche(self):
        """Méthode qui met à jour le navire quand il est touché"""
        self.nb_touche = self.nb_touche+1
        # Si toutes les cases du navire sont touchées, on le note Coulé
        if self.nb_touche == self.length_ship:
            self.is_coule = True

    @staticmethod
    def get_list_ships():
        """ Fonction qui renvoie la liste des navires"""
        return Ship.ships_list

    @staticmethod
    def get_ship_cases():
        """Fonction qui récupère les coordonnées des cases de tous les navires """
        ship_cases = {}
        # Je parcours ma liste de navires
        for ship in Ship.ships_list:
            # list_cases = get_list_cases_by_ship(ship['first_case'], ship['sens'], ship['length_ship'])
            list_cases = ship.get_list_cases()
            ship.list_cases = list_cases
            # On ajoute la liste des coordonnées de ce navire à la liste globale des coordonnées
            for case in ship.list_cases:
                ship_cases[case] = const.CONST_INTACT
        return ship_cases