from modele.joueur import Joueur
from views.display import Affichage
from tinydb import TinyDB
from pathlib2 import Path

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / 'database' / 'joueurs.json'


class Display:
    def __init__(self):
        self.liste_joueurs = []
        self.db = TinyDB(db_path)

    def charger_joueurs(self):
        joueurs = self.db.table("_default").all()
        joueurs_tries = sorted(joueurs, key=lambda joueur: joueur["Nom"])
        # print("Charger joueur : ")
        # print(joueurs)
        for joueur in joueurs_tries:
            self.liste_joueurs.append(
                Joueur(joueur["Nom"], joueur["Prénom"], joueur["Date de naissance"], joueur["ID"]))
            # print(f'{joueur["Nom"]} {joueur["Prénom"]}')

    def afficher_liste_joueurs(self):
        affichage = Affichage()
        affichage.afficher_liste_joueurs(self.liste_joueurs)
