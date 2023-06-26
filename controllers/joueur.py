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
        """Charge les joueurs depuis la base de données et les stocke dans une liste"""
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
        """Affiche la liste des joueurs stockés dans la liste"""
        affichage = Affichage()
        affichage.afficher_liste_joueurs(self.liste_joueurs)

    def selectionner_joueurs(self, nb_joueurs: int):
        """Sélectionne aléatoirement un nombre de joueurs donné dans la liste des joueurs existants"""
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

        return liste_joueurs_selectionnes
