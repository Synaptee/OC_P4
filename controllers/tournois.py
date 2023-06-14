from modele.tournois import Tournoi
from views.reports import Affichage
from tinydb import TinyDB, Query
from pathlib2 import Path
import random
import datetime

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

    @staticmethod
    def display_rounds_matchs_tournoi(rounds: dict):
        affichage = Affichage()
        affichage.afficher_rounds_matchs_tournois(rounds)

    @staticmethod
    def get_current_round(id_tournoi):
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        instance_round = tournoi_en_cours[0]["Tour actuel"]
        round_datas = tournoi_en_cours[0]["Tours"]["Round " + str(instance_round)]
        print(round_datas, instance_round)
        return round_datas, instance_round

    def generate_random_matches(self, id_tournoi: str = ""):
        """Generate random matches for the first round of a tournament"""
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
        matches[round_name] = {}
        matches[round_name]["Start"] = str(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        )
        matches[round_name]["Matchs"] = []
        matches[round_name]["End"] = ""

        # Création des paires de joueurs
        for i in range(0, num_players, 2):
            match = ([player_list[i], 0], [player_list[i + 1], 0])
            matches[round_name]["Matchs"].append(match)
        # print(matches)
        updated_tournoi = tournoi_en_cours[0]
        updated_tournoi["Tour actuel"] = 1
        updated_tournoi["Tours"] = matches
        # print(updated_tournoi)
        self.table.update(updated_tournoi, Query().ID == id_tournoi)

        # return matches
