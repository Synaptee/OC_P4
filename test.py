import random
from tinydb import TinyDB
from modele.joueur import Joueur


def create_random_player_list(num_players):
    db = TinyDB("/Users/jbstudio/Desktop/DA_Python/OC_P4/database/joueurs.json")
    players = db.table("_default")
    player_data = players.all()

    # Vérification si le nombre demandé est supérieur au nombre total de joueurs disponibles
    if num_players > len(player_data):
        raise ValueError(
            "Le nombre de joueurs demandé dépasse le nombre total de joueurs disponibles."
        )

    # Sélection aléatoire des joueurs
    selected_players = random.sample(player_data, num_players)

    # Création de la liste de noms et prénoms des joueurs sélectionnés
    player_list = []
    for player in selected_players:
        nom_prenom = f"{player['Nom']} {player['Prénom']}"
        player_list.append(nom_prenom)

    return player_list


# Exemple d'utilisation
num_joueurs_demandes = int(input("Combien de joueurs voulez-vous ? "))
liste_joueurs = create_random_player_list(num_joueurs_demandes)
print(liste_joueurs)


def generate_random_matches(player_list):
    num_players = len(player_list)

    # Vérification si le nombre de joueurs est impair
    if num_players % 2 != 0:
        raise ValueError("Le nombre de joueurs doit être pair pour générer des matchs.")

    random.shuffle(player_list)  # Mélange aléatoire des joueurs

    matches = {}
    round_name = "round 1"
    matches[round_name] = []

    # Création des paires de joueurs
    for i in range(0, num_players, 2):
        match = (player_list[i], player_list[i + 1])
        matches[round_name].append(match)

    return matches


# Exemple d'utilisation
print("***")
# matchs = generate_random_matches(liste_joueurs)
# print(matchs)

nom = input("Saisissez le nom du joueur : ")
prenom = input("Saisissez le prénom du joueur : ")
date_de_naissance = input("Saisissez la date de naissance du joueur : ")
id_national = input("Saisissez l'ID national du joueur : ")

joueur = Joueur(nom, prenom, date_de_naissance, id_national)
print(joueur)
