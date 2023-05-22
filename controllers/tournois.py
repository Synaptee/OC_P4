from modele.tournois import Tournoi
from views.display import Affichage
from tinydb import TinyDB
from pathlib2 import Path

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / 'database' / 'tournois.json'


class DisplayTournois:
    def __init__(self):
        self.liste_tournois = []
        self.db = TinyDB(db_path)

    def charger_tournois(self):
        tournois = self.db.table("_default").all()
        # print("Charger joueur : ")
        # print(joueurs)
        for tournoi in tournois:
            self.liste_tournois.append(
                Tournoi(tournoi["Nom"], tournoi["Lieu"], tournoi["Date de début"], tournoi["Date de fin"], tournoi["Nombre de tours"], tournoi["Tour actuel"], tournoi["Tours"], tournoi["Joueurs"], tournoi["Description"]))
            

    def afficher_liste_tournois(self):
        affichage = Affichage()
        affichage.afficher_liste_tournois(self.liste_tournois)