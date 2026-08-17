#!/usr/bin/env python
# -*- coding: utf-8 -*-

import constantes as const
from grid import Grid
from ship import Ship
import random

"""
Bataille navale
Séverine Hori Maitrehut
"""

def naval_battle():
    print("*********************************** Bataille navalle ********************************************")
    # On initialise la grille et ses navires
    grid = Grid()    
    
    # Initialisation à vide le la liste des tirs manqués de l'utilisateur
    is_end_session = False

    # On affiche la grille - pour l'instant à vide
    grid.display()

    while not is_end_session:
        # On demande à l'utilisateur les coordonnées de son tir
        coordonnees_tir = Grid.get_coordonnees_input()

        #Le tir est envoyé sur la grille
        grid.tir(coordonnees_tir)

        # Affichage de la grille avec informations sur les cases touchées, coulées, ratées...
        grid.display()

        # Si on a coulé tous les navires on arrête le programme
        if grid.nb_sunken_ship >= const.CONST_NB_SHIPS:
            print("Vous avez coulé tous les navires, la partie est terminée. Bravo ! ")
            is_end_session = True

if __name__ == '__main__':
    naval_battle()