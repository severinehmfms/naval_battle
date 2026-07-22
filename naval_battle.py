#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import constantes as const
from ship import Ship

"""
Bataille navale
Séverine Hori Maitrehut
"""


def is_coordonnees_ok(saisie):
    """Fonction qui teste si la saisie de l'utilisateur est correcte"""
    cleaned_saisie = saisie.strip()
    if not cleaned_saisie.isalnum():
        return False
    # On teste si on a bien une lettre entre a et j en entrée
    if cleaned_saisie[0] not in const.columns_alpha_list:
        print("Le premier caractère saisi doit être une lettre entre A et J")
        return False
    # On teste si la suite de la saisie est bien un numérique
    if not cleaned_saisie[1:].isdigit():
        print("Le second caractère saisi doit être un chiffre")
        return False
    # On teste si le numérique est bien entre 1 et 10
    if int(cleaned_saisie[1:]) < 1 or int(cleaned_saisie[1:]) > 10:
        print("Le second caractère saisi doit être un chiffre entre 1 et 10")
        return False
    return True


def get_coordonnees_input():
    """Fonction qui demande à l'utilisateur de saisir les coordonnées de son tir"""
    coordonnees_tir = input("Saisir les coordonnées du tir (Lettre A et J + nombre entre 0 et 10. Pas d'espace.) : ")
    while not is_coordonnees_ok(coordonnees_tir.strip()):
        coordonnees_tir = input("Saisie incorrecte. Merci de recommencer : ")
    return coordonnees_tir


def print_game_grid(ship_cases, missed_shot):
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
            if case_en_cours in ship_cases:
                if ship_cases[case_en_cours] == const.CONST_INTACT:
                    line_print += " " + const.CONST_AFF_INTACT + " |"
                elif ship_cases[case_en_cours] == const.CONST_TOUCHE:
                    line_print += " " + const.CONST_AFF_TOUCHE + " |"
                elif ship_cases[case_en_cours] == const.CONST_COULE:
                    line_print += " " + const.CONST_AFF_COULE + " |"
            # On regarde si cette case en cours fait partie des tirs manqués (présence dans missed_shot)
            elif case_en_cours in missed_shot:
                line_print += " " + const.CONST_AFF_DEJA_TIRE + " |"
            else:
                line_print += "   |"
        print(line_print)
    print(dividor_line)


def init_ship():
    ship1 = Ship("aircraft_carrier", 5, const.CONST_HORIZONTAL, "B2")
    ship2 = Ship("cruiser", 4, const.CONST_VERTICAL, "A4")
    ship3 = Ship("destroyer", 3, const.CONST_VERTICAL, "C5")
    ship4 = Ship("submarine", 3, const.CONST_HORIZONTAL, "H5")
    ship5 = Ship("torpedo_boat", 2, const.CONST_HORIZONTAL, "E9")

if __name__ == '__main__':
    print("*********************************** Bataille navalle ********************************************")
    ship_list = []
    ship_cases = {}

    # Initialisation de la liste des navires
    init_ship()
    # Récupération de la liste des navires
    ship_list = Ship.ships_list
    # Initialisation de la liste des coordonnées de toutes les cases de tous les navires
    ship_cases = Ship.get_ship_cases()
    # Initialisation à vide le la liste des tirs manqués de l'utilisateur
    missed_shot = []
    is_end_session = False
    nb_sunken_ship = 0

    # On affiche la grille - pour l'instant à vide
    print_game_grid(ship_cases, missed_shot)

    while not is_end_session:
        # On demande à l'utilisateur les coordonnées de ses tirs
        coordonnees_tir = get_coordonnees_input()

        # On va voir si les coordonnées du tir figurent dans la liste des cases de tous les navires
        if coordonnees_tir in ship_cases:
            if ship_cases[coordonnees_tir] == const.CONST_TOUCHE:
                print("Emplacement déjà touché précédemment. ")
            elif ship_cases[coordonnees_tir] == const.CONST_COULE:
                print("Navire déjà coulé précédemment.")
            else:
                print("On a touché un navire, on passe là")
                # On a touché un navire
                ship_cases[coordonnees_tir] = const.CONST_TOUCHE
                # On récupère le navire touché
                ship_touched = Ship.tir(coordonnees_tir)
                # Je mets à jour le navire touché
                ship_touched.touche()
                if ship_touched.is_coule:
                    # Si coulé, pour chaque case de ce navire dans ship_cases je mets le statut Coulé
                    for macase in ship_touched.list_cases:
                        ship_cases[macase] = const.CONST_COULE
                    print(f"Navire {ship_touched.name} coulé !")
                    nb_sunken_ship += 1
                else:
                    print("Touché ! ")
        else:
            print("Tir manqué ! ")
            missed_shot.append(coordonnees_tir)

        # Affichage de la grille avec informations sur les cases touchées, coulées, ratées...
        print_game_grid(ship_cases, missed_shot)

        # Si on a coulé tous les navires on arrête le programme
        if nb_sunken_ship >= 5:
            print("Vous avez coulé tous les navires, la partie est terminée. Bravo ! ")
            is_end_session = True