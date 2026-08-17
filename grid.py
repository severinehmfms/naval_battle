from dataclasses import dataclass
import constantes as const
from ship import Ship
import random

""" Classe Grid qui représente un bateau"""

@dataclass
class Grid:
    ships_list : []
    ships_cases : {}
    missed_shot = []
    nb_sunken_ship = 0
    
    def __init__(self):
        """Méthode d'initialisation de la grille et de ses bateaux"""
        self.init_ship_aleatoire()
        
        #On initialise la liste des bateaux
        self.ships_list = Ship.ships_list
        
        # On initialise aussi la liste des coordonnées de toutes les cases occupées par des bateaux
        self.ship_cases = self.get_ship_cases()
 
    def display(self):
        """Fonction qui affiche la grille de jeu Bataille navale"""

        # Ligne de séparation
        dividor_line = ""
        for _ in range(11):
            dividor_line += "+---"
        dividor_line += "+"
        print(dividor_line)

        # Ligne des colonnes
        columns_line = "|   |"
        for lettre in const.columns_alpha_list:
            columns_line += " "
            columns_line += lettre.upper()
            columns_line += " |"
        print(columns_line)

        for num_ligne in range(1, 11):
            print(dividor_line)

            # On ajoute le numéro de la ligne
            line_print = "|"
            if num_ligne != 10:
                line_print += " "
            line_print += str(num_ligne) + " |"

            for num_colonne in range(0, 10):
                lettre_en_cours = const.columns_alpha_list[num_colonne]
                case_en_cours = lettre_en_cours + str(num_ligne)
                # On regarde si cette case en cours est Touchée ou Coulée ou Intacte dans ship_cases
                if case_en_cours in self.ship_cases:
                    if self.ship_cases[case_en_cours] == const.CONST_INTACT:
                        line_print += " " + const.CONST_AFF_INTACT + " |"
                    elif self.ship_cases[case_en_cours] == const.CONST_TOUCHE:
                        line_print += " " + const.CONST_AFF_TOUCHE + " |"
                    elif self.ship_cases[case_en_cours] == const.CONST_COULE:
                        line_print += " " + const.CONST_AFF_COULE + " |"
                # On regarde si cette case en cours fait partie des tirs manqués (présence dans missed_shot)
                elif case_en_cours in self.missed_shot:
                    line_print += " " + const.CONST_AFF_DEJA_TIRE + " |"
                else:
                    line_print += "   |"
            print(line_print)
        print(dividor_line)
    
    def tir(self,coordonnees_tir):
        """ Méthode qui en fonction des coordonnées du tir du joueur
        va regarder si un bateau est touché, coulé, ou si le tir est raté
        """
        # On va voir si les coordonnées du tir figurent dans la liste des cases de tous les navires
        if coordonnees_tir in self.ship_cases:
            if self.ship_cases[coordonnees_tir] == const.CONST_TOUCHE:
                print("Emplacement déjà touché précédemment. ")
            elif self.ship_cases[coordonnees_tir] == const.CONST_COULE:
                print("Navire déjà coulé précédemment.")
            else:
                # On a touché un navire
                self.ship_cases[coordonnees_tir] = const.CONST_TOUCHE
                # On récupère le navire touché par le tir
                ship_touched = Ship.get_ship_touched(coordonnees_tir)
                if ship_touched.is_coule:
                    # Si coulé, pour chaque case de ce navire dans ship_cases je mets le statut Coulé
                    for macase in ship_touched.list_cases:
                        self.ship_cases[macase] = const.CONST_COULE
                    print(f"Navire {ship_touched.name} coulé !")
                    self.nb_sunken_ship += 1
                else:
                    print("Touché ! ")
        else:
            print("Tir manqué ! ")
            self.missed_shot.append(coordonnees_tir)
    
    def init_ship(self):
        """ Initialisatoin des navires, en dur """
        _ = Ship("aircraft_carrier", 5, const.CONST_HORIZONTAL, "B2")
        _ = Ship("cruiser", 4, const.CONST_VERTICAL, "A4")
        _ = Ship("destroyer", 3, const.CONST_VERTICAL, "C5")
        _ = Ship("submarine", 3, const.CONST_HORIZONTAL, "H5")
        _ = Ship("torpedo_boat", 2, const.CONST_HORIZONTAL, "E9")
        
    def init_ship_aleatoire(self):
        """ Initialisation de manière aléatoire des navires """
        cases_used = []
        # On parcoure les bateaux à créer
        for infos_bateau in const.CONST_NAME_SHIP:
            is_to_created = False
            # Tant qu'il n'y a pas d'erreur pour la création du bateau
            while not is_to_created:
                choice_col = random.randint(0, const.CONST_TAILLE_GRID-1)
                choice_line = random.randint(1, const.CONST_TAILLE_GRID)
                coordonnees = self.convert_num_column_to_letter(choice_col)+str(choice_line)
                sens = random.choice([const.CONST_HORIZONTAL, const.CONST_VERTICAL])
                is_to_created = True

                # On vérifie que le bateau ne dépasse pas les limites de la grille (si horizontal, grille horizontale)
                if (sens == const.CONST_HORIZONTAL and choice_col > const.CONST_TAILLE_GRID-infos_bateau[1]):
                    #print(f"Le sens est {sens} et le numéro de colonne est {choice_col} ({self.convert_num_column_to_letter(choice_col)}) Taille du bateau : {infos_bateau[1]} on recommence")
                    is_to_created = False
                # On vérifie que le bateau ne dépasse pas les limites de la grille (si horizontal, grille verticale)
                elif (sens == const.CONST_VERTICAL and choice_line > const.CONST_TAILLE_GRID-infos_bateau[1]):
                    #print(f"Le sens est {sens} et le numéro de ligne est {choice_line} Taille du bateau : {infos_bateau[1]} on recommence")
                    is_to_created = False
                # On vérifie que le bateau ne va pas rentrer en collision avec un des bateaux créés précédemment
                else:
                    cases_of_new_ship = Ship.get_list_cases_by_first(coordonnees,sens,infos_bateau[1])
                    for case in cases_of_new_ship:
                        if case in cases_used:
                            #print("Ce bateau va écraser un autre bateau, on recommence : case {case}")
                            is_to_created = False

                # Si tout est ok, on va pouvoir créer le bateau et sortir de la boucle
                if (is_to_created):
                    print(f"On va initialiser le bateau {infos_bateau[0]}, Longueur {infos_bateau[1]}, Sens {sens}, Première case {coordonnees} ")
                    ship = Ship(infos_bateau[0], int(infos_bateau[1]), sens, coordonnees)
                    #On ajoute le bateau ainsi créé dans cases_used
                    cases_used.append(ship.list_cases)
                    is_to_created = True
    
    def get_ship_cases(self):
        """Fonction qui récupère les coordonnées des cases de tous les navires
         ATTENTION Elles sont initialisées à INTACTES (pour début de partie)
         Le but de ce dictionnaire est de simplifier l'affichage de la grille
         """
        ship_cases = {}
        # Je parcours ma liste de navires
        for ship in self.ships_list:
            list_cases = Ship.get_list_cases_by_first(ship.first_case, ship.sens, ship.length_ship)
            ship.list_cases = list_cases
            # On ajoute la liste des coordonnées de ce navire à la liste globale des coordonnées
            for case in ship.list_cases:
                ship_cases[case] = const.CONST_INTACT
        return ship_cases
    
    @staticmethod
    def is_coordonnees_ok(saisie):
        """Fonction qui teste si la saisie de l'utilisateur est correcte"""
        cleaned_saisie = saisie.strip()
        if not cleaned_saisie.isalnum():
            return False
        # On teste si on a bien une lettre entre a et j en entrée
        if cleaned_saisie[0] not in const.columns_alpha_list:
            print(f"Le premier caractère saisi doit être une lettre entre A et {const.columns_alpha_list[-1]}")
            return False
        # On teste si la suite de la saisie est bien un numérique
        if not cleaned_saisie[1:].isdigit():
            print("Le second caractère saisi doit être un chiffre")
            return False
        # On teste si le numérique est bien entre 1 et la taille de la grille
        if int(cleaned_saisie[1:]) < 1 or int(cleaned_saisie[1:]) > const.CONST_TAILLE_GRID:
            print(f"Le second caractère saisi doit être un chiffre entre 1 et {const.CONST_TAILLE_GRID}")
            return False
        return True

    @staticmethod
    def get_coordonnees_input():
        """Fonction qui demande à l'utilisateur de saisir les coordonnées de son tir"""
        coordonnees_tir = input(f"Saisir les coordonnées du tir (Lettre A et J + nombre entre 0 et {const.CONST_TAILLE_GRID}. Pas d'espace.) : ")
        while not Grid.is_coordonnees_ok(coordonnees_tir.strip()):
            coordonnees_tir = input("Saisie incorrecte. Merci de recommencer : ")
        return coordonnees_tir

    @staticmethod
    def convert_num_column_to_letter(num):
        """ Fonction qui convertit un numéro de lettre en lettre """
        return const.columns_alpha_list[num]

    @staticmethod
    def convert_letter_to_num_column(letter):
        """ Fonction qui convertit une lettre en numéro de lettre """
        return const.columns_alpha_list.index(letter)

    