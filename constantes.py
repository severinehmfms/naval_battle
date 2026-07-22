import string

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
columns_alpha_list = alphabet_list[:10]