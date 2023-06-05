import random
from tinydb import TinyDB
from modele.joueur import Joueur


def generate_random_matches(player_list):
    num_players = len(player_list)

    # Vérification si le nombre de joueurs est impair
    if num_players % 2 != 0:
        raise ValueError("Le nombre de joueurs doit être pair pour générer des matchs.")

    random.shuffle(player_list)  # Mélange aléatoire des joueurs

    matches = {}
    round_name = "Round 1"
    matches[round_name] = []

    # Création des paires de joueurs
    for i in range(0, num_players, 2):
        match = ([player_list[i], 0], [player_list[i + 1], 0])
        matches[round_name].append(match)

    return matches


# Exemple d'utilisation
print("***")
liste_joueurs = [
    "Larchevque Eric",
    "Hamilton Lewis",
    "Kasparov Garry",
    "Ocean Daniel",
    "Boursier K\u00e9vin",
    "Carlsen Magnus",
]
matchs = generate_random_matches(liste_joueurs)
print(matchs)
