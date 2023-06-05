from modele.joueur import Joueur
from views.reports import Affichage
from tinydb import TinyDB
from pathlib2 import Path
import random

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / "database" / "joueurs.json"


class ControllerJoueur:
    def __init__(self):
        self.liste_joueurs = []
        self.db = TinyDB(db_path)

    def charger_joueurs(self):
        joueurs = self.db.table("_default").all()
        joueurs_tries = sorted(joueurs, key=lambda joueur: joueur["Nom"])
        for joueur in joueurs_tries:
            self.liste_joueurs.append(
                Joueur(
                    joueur["Nom"],
                    joueur["Prénom"],
                    joueur["Date de naissance"],
                    joueur["ID"],
                )
            )

    def afficher_liste_joueurs(self):
        affichage = (
            Affichage()
        )  # Initule de créer une instance de la classe Affichage puisque j'appelle une @staticmethod
        affichage.afficher_liste_joueurs(self.liste_joueurs)

    def selectionner_joueurs(self, nb_joueurs):
        joueurs = self.db.table("_default").all()
        if nb_joueurs > len(joueurs):
            raise ValueError(
                "Le nombre de joueurs demandé dépasse le nombre total de joueurs disponibles."
            )

        joueurs_selectionnes = random.sample(joueurs, nb_joueurs)

        liste_joueurs_selectionnes = []
        for player in joueurs_selectionnes:
            nom_prenom = f"{player['Nom']} {player['Prénom']}"
            liste_joueurs_selectionnes.append(nom_prenom)

        print(liste_joueurs_selectionnes)
        return liste_joueurs_selectionnes

    def generate_random_players_list(self, nb_joueurs):
        player_data = self.db.table("_default").all()

        # Vérification si le nombre demandé est supérieur au nombre total de joueurs disponibles
        if nb_joueurs > len(player_data):
            raise ValueError(
                "Le nombre de joueurs demandé dépasse le nombre total de joueurs disponibles."
            )

        # Sélection aléatoire des joueurs
        selected_players = random.sample(player_data, nb_joueurs)

        # Création de la liste de noms et prénoms des joueurs sélectionnés
        player_list = []
        for player in selected_players:
            nom_prenom = f"{player['Nom']} {player['Prénom']}"
            player_list.append(nom_prenom)

        # return player_list
        print(player_list)
