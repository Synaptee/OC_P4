from modele.tournois import Tournoi
from views.reports import Affichage
from tinydb import TinyDB, Query
from pathlib2 import Path

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / "database" / "tournois.json"


class ControllerTournoi:
    db = TinyDB(db_path)
    table = db.table("_default")

    def __init__(self):
        self.liste_tournois = []

    def charger_tournois(self):
        tournois = self.db.table("_default").all()
        for tournoi in tournois:
            self.liste_tournois.append(
                Tournoi(
                    tournoi["Nom"],
                    tournoi["Lieu"],
                    tournoi["Date de début"],
                    tournoi["Date de fin"],
                    tournoi["Nombre de tours"],
                    tournoi["Tour actuel"],
                    tournoi["Tours"],
                    tournoi["Joueurs"],
                    tournoi["Description"],
                )
            )

    def afficher_liste_tournois(self):
        affichage = Affichage()
        affichage.afficher_liste_tournois(self.liste_tournois)

    @staticmethod
    def get_tournoi(id_tournoi):
        tournoi_en_cours = ControllerTournoi.table.search((Query().ID == id_tournoi))
        affichage = Affichage()
        affichage.afficher_infos_tournois(tournoi_en_cours)

    @staticmethod
    def get_joueurs_tournoi(id_tournoi):
        tournoi_en_cours = ControllerTournoi.table.search((Query().ID == id_tournoi))
        affichage = Affichage()
        affichage.afficher_liste_joueurs_tournoi(tournoi_en_cours)
