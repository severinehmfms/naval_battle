import string

# Constantes pour le nombre de lignes et de colonnes de la grille
CONST_TAILLE_GRID = 10
CONST_NB_SHIPS = 5

# Constantes pour les statuts
CONST_TOUCHE, CONST_COULE, CONST_INTACT = "Touché", "Coulé", "Intact"

# Constantes pour l'affichage dans la grille
CONST_AFF_TOUCHE, CONST_AFF_COULE, CONST_AFF_INTACT, CONST_AFF_DEJA_TIRE,   = "X", "°", " ", "-"

# Constantes pour le sens Horizontal ou Vertical
CONST_HORIZONTAL = "H"
CONST_VERTICAL = "V"

# Lettres de l'alphabet puis titres des colonnes (pour l'instant les 10 premières mais c'est évolutif)
english_alphabet_string_uppercase = string.ascii_uppercase
alphabet_list = list(english_alphabet_string_uppercase)
columns_alpha_list = alphabet_list[:CONST_TAILLE_GRID]

#Informations fixes sur les bateaux
CONST_NAME_SHIP = [["aircraft_carrier", 5], ["cruiser", 4], ["destroyer", 3], ["submarine", 3], ["torpedo_boat", 2]]
