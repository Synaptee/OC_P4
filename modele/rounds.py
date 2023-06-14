from tinydb import TinyDB, Query
from pathlib2 import Path
import random
import datetime

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / "database" / "tournois.json"


# tournois = table.all()
# Récupérer la liste des rounds en cours
# id_tournoi = "BLP2223"


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

        # Vérification si le nombre de joueurs est impair
        if num_players % 2 != 0:
            raise ValueError(
                "Le nombre de joueurs doit être pair pour générer des matchs."
            )

        random.shuffle(player_list)  # Mélange aléatoire des joueurs

        matches = {}
        self.name = "Round 1"
        # matches[round_name] = []

        # Création des paires de joueurs
        for i in range(0, num_players, 2):
            match = ([player_list[i], 0], [player_list[i + 1], 0])
            self.matchs.append(match)
        # print(matches)

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
        # updated_round_results = tournoi_en_cours[0]
        self.matchs = round_results
        print(self.matchs)
        self.end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        # print(round_results)
        # print(updated_round_results)
        # table.update(updated_round_results, Query().ID == id_tournoi)
        # print("Résultats du round enregistrés")

    def save_round_results(self, id_tournoi: str = ""):
        """Function that save round results in the database"""
        tournoi_en_cours = self.table.search((Query().ID == id_tournoi))
        updated_tournoi = tournoi_en_cours[0]
        updated_tournoi["Tours"][self.name]["Matchs"] = self.matchs
        updated_tournoi["Tours"][self.name]["End"] = self.end_date
        updated_tournoi["Tour actuel"] += 1
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
        tour = item["Tours"]
        new_round = {}
        new_round["Start"] = self.start_date
        new_round["Matchs"] = self.matchs
        new_round["End"] = self.end_date
        tour[self.name] = new_round
        print(self.name)
        print(f"Le tour est : {tour}")
        self.db.update({"Tours": tour}, doc_ids=[item.doc_id])
        # tournoi_en_cours = table.search((Query().ID == self.tournament_id))
        # tournoi_en_cours[0]["Tours"][self.name] = new_round

        # self.db.insert({"ID": self.tournament_id, "Tours": {self.name: new_round}})

        print("Nouveau round enregistré")


# Récupérer la liste des rounds en cours
# id_tournoi = "BLP2223"

# tournoi_en_cours = table.search((Query().ID == id_tournoi))
# matchs = tournoi_en_cours[0]["Tours"]["Round 2"]
# print(f'Le nom du round est {nom_round}')


# Current_Round = Round(tournament_id="BLP2223")
# # Current_Round.enter_round_results()
# Current_Round.generate_first_round()
# print(Current_Round.matchs)
# print(Current_Round.start_date)
