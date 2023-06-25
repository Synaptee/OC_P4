from tinydb import TinyDB, Query
from pathlib2 import Path
import random
import datetime

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / "database" / "tournois.json"


class Round:
    db = TinyDB(db_path)
    table = db.table("_default")

    def __init__(
        self,
        name: str = "",
        start_date: str = "",
        end_date: str = "",
        matchs: list = [],
        tournament_id: str = "",
    ):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matchs = matchs
        self.tournament_id = tournament_id

    def generate_first_round(self):
        """Function that generates the first round of a tournament"""
        tournament_datas = self.table.search((Query().ID == self.tournament_id))
        player_list = tournament_datas[0]["Joueurs"]
        num_players = len(player_list)

        if num_players % 2 != 0:
            raise ValueError(
                "Le nombre de joueurs doit être pair pour générer des matchs."
            )

        random.shuffle(player_list)

        self.name = "Round 1"

        for i in range(0, num_players, 2):
            match = ([player_list[i], 0], [player_list[i + 1], 0])
            self.matchs.append(match)

        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    def enter_round_results(self):
        """Function that enables you to enter round matches resutlts"""
        round_results = []
        for match in self.matchs:
            print("\n Indiquez le vainqueur du match : ")
            print(f"{match[0][0]} (1) ou {match[1][0]} (2)")
            print("Indiquer 0 pour match nul")
            result = input("Saisissez le résultat : ")

            if result == "1":
                match[0][1] += 1
            elif result == "2":
                match[1][1] += 1
            elif result == "0":
                match[0][1] += 0.5
                match[1][1] += 0.5
            else:
                print("Saisie invalide")

            round_results.append(match)

        self.matchs = round_results
        self.end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    def save_round_results(self, id_tournoi: str = ""):
        """Function that save round results in the database"""
        tournoi_en_cours = self.table.search((Query().ID == id_tournoi))
        updated_tournoi = tournoi_en_cours[0]
        updated_tournoi["Tours"][self.name]["Matchs"] = self.matchs
        updated_tournoi["Tours"][self.name]["End"] = self.end_date
        # updated_tournoi["Tour actuel"] += 1
        self.table.update(updated_tournoi, Query().ID == id_tournoi)
        print("Résultats du round enregistrés")

    def get_played_rounds(self) -> list:
        """Function that returns the list of played rounds"""
        tournoi_en_cours = self.table.search((Query().ID == self.tournament_id))
        played_rounds = []
        round_en_cours = int(tournoi_en_cours[0]["Tour actuel"])

        for i in range(1, round_en_cours + 1):
            played_rounds.append(
                tournoi_en_cours[0]["Tours"]["Round " + str(round_en_cours)]["Matchs"][
                    0
                ]
            )

        return played_rounds

    def save_new_round(self):
        item = self.db.get(Query().ID == self.tournament_id)
        print(item)
        tour = item["Tours"]
        new_round = {}
        new_round["Start"] = self.start_date
        new_round["Matchs"] = self.matchs
        new_round["End"] = self.end_date
        tour[self.name] = new_round
        print(self.name)
        print(f"Le tour est : {tour}")
        self.db.update({"Tours": tour}, doc_ids=[item.doc_id])

        print("Nouveau round enregistré")
