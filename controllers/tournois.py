from modele.tournois import Tournoi
from views.reports import Affichage
from tinydb import TinyDB, Query
from pathlib2 import Path
import random

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
    def search_tournoi(id_tournoi):
        tournoi_en_cours = ControllerTournoi.table.search((Query().ID == id_tournoi))
        return tournoi_en_cours

    @staticmethod
    def get_tournoi(id_tournoi):
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        affichage = Affichage()
        affichage.afficher_infos_tournois(tournoi_en_cours)

    @staticmethod
    def get_joueurs_tournoi(id_tournoi):
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        affichage = Affichage()
        affichage.afficher_liste_joueurs_tournoi(tournoi_en_cours)

    def generate_random_matches(self, id_tournoi: str):
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        player_list = tournoi_en_cours[0]["Joueurs"]
        num_players = len(player_list)

        # Vérification si le nombre de joueurs est impair
        if num_players % 2 != 0:
            raise ValueError(
                "Le nombre de joueurs doit être pair pour générer des matchs."
            )

        random.shuffle(player_list)  # Mélange aléatoire des joueurs

        matches = {}
        round_name = "Round 1"
        matches[round_name] = []

        # Création des paires de joueurs
        for i in range(0, num_players, 2):
            match = ([player_list[i], 0], [player_list[i + 1], 0])
            matches[round_name].append(match)
        # print(matches)
        updated_tournoi = tournoi_en_cours[0]
        updated_tournoi["Tour actuel"] = 1
        updated_tournoi["Tours"] = matches
        print(updated_tournoi)
        Entry = Query()
        self.table.update(updated_tournoi, Entry.ID == id_tournoi)

        # return matches
