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
        """Charger les tournois depuis la base de données et les stocker dans une liste"""
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
        """Afficher la liste des tournois stockés dans la base de données"""
        affichage = Affichage()
        affichage.afficher_liste_tournois(self.liste_tournois)

    def filtrer_tournois_en_cours(self):
        """Filtrer et afficher les tournois en cours"""
        tournois_en_cours = []
        for tournoi in self.liste_tournois:
            if tournoi.tour_actuel != tournoi.nombre_de_tours:
                tournois_en_cours.append(tournoi)
        affichage = Affichage()
        affichage.afficher_liste_tournois(tournois_en_cours)

    @staticmethod
    def search_tournoi(id_tournoi):
        """Rechercher un tournoi dans la base de données par son ID"""
        tournoi_en_cours = ControllerTournoi.table.search((Query().ID == id_tournoi))
        return tournoi_en_cours

    @staticmethod
    def get_tournoi(id_tournoi):
        """Récupérer un tournoi dans la base de données par son ID et l'afficher"""
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        affichage = Affichage()
        affichage.afficher_infos_tournois(tournoi_en_cours)

    @staticmethod
    def get_joueurs_tournoi(id_tournoi):
        """Récupérer les joueurs d'un tournoi donné dans la base de données et l'afficher"""
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        affichage = Affichage()
        affichage.afficher_liste_joueurs_tournoi(tournoi_en_cours)

    @staticmethod
    def display_rounds_matchs_tournoi(rounds: dict):
        """Affiche tous les rounds et les matchs d'un tournoi donné"""
        affichage = Affichage()
        affichage.afficher_rounds_matchs_tournois(rounds)

    @staticmethod
    def get_current_round(id_tournoi):
        """Récupère le round actuel d'un tournoi donné"""
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        instance_round = str(tournoi_en_cours[0]["Tour actuel"])
        round_datas = tournoi_en_cours[0]["Tours"]["Round " + str(instance_round)]
        return round_datas, instance_round

    def check_if_players(self, id_tournoi: str = ""):
        """Vérifie si des joueurs ont été ajoutés à un tournoi donné"""
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        if tournoi_en_cours[0]["Joueurs"] == []:
            return False
        else:
            return True

    def sauvegarde_joueurs(self, id_tournoi: str = "", joueurs: list = []):
        item = self.db.get(Query().ID == id_tournoi)
        joueurs_inscrits = item["Joueurs"]

        for joueur in joueurs:
            joueurs_inscrits.append(joueur)
        self.db.update({"Joueurs": joueurs_inscrits}, doc_ids=[item.doc_id])

    def generate_random_matches(self, id_tournoi: str = ""):
        """Génére des matchs aléatoires pour le premier round d'un tournoi donné"""
        tournoi_en_cours = ControllerTournoi.search_tournoi(id_tournoi)
        player_list = tournoi_en_cours[0]["Joueurs"]
        num_players = len(player_list)

        if num_players % 2 != 0:
            raise ValueError(
                "Le nombre de joueurs doit être pair pour générer des matchs."
            )

        random.shuffle(player_list)

        matches = {}
        round_name = "Round 1"
        matches[round_name] = {}
        matches[round_name]["Start"] = str(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        )
        matches[round_name]["Matchs"] = []
        matches[round_name]["End"] = ""

        for i in range(0, num_players, 2):
            match = ([player_list[i], 0], [player_list[i + 1], 0])
            matches[round_name]["Matchs"].append(match)
        updated_tournoi = tournoi_en_cours[0]
        updated_tournoi["Tour actuel"] = 1
        updated_tournoi["Tours"] = matches
        self.table.update(updated_tournoi, Query().ID == id_tournoi)

    def update_current_round(self, id_tournoi, current_round):
        """Mise à jour du round actuel d'un tournoi donné dans la base de données"""
        item = self.db.get(Query().ID == id_tournoi)
        current_tour = item["Tour actuel"]
        current_tour = current_tour + 1
        self.db.update({"Tour actuel": current_tour}, doc_ids=[item.doc_id])

    def already_played(self, matchs_en_cours, joueur1, joueur2):
        """Vérifie si deux joueurs ont déjà joué ensemble lors d'un tournoi donné"""
        for match in matchs_en_cours:
            print(f"Le match est : {match}")
            if (joueur1 in match[0] or joueur1 in match[1]) and (
                joueur2 in match[0] or joueur2 in match[1]
            ):
                return True
        return False

    def organiser_matchs(self, joueurs, matchs_joues):
        """Organisation des matchs d'un tournoi donné (en dehors du round 1)"""
        matchs_futurs = []
        joueurs_points = {}

        for joueur in joueurs:
            points = 0
            for match in matchs_joues:
                if match[0][0] == joueur:
                    points += match[0][1]
                elif match[1][0] == joueur:
                    points += match[1][1]
            joueurs_points[joueur] = points


        joueurs_tries = sorted(joueurs, key=lambda x: joueurs_points[x], reverse=True)

        while len(joueurs_tries) != 0:
            i = 0
            joueur1 = joueurs_tries[i]
            joueur2 = joueurs_tries[i + 1] if i + 1 < len(joueurs_tries) else None

            while joueur2 and self.already_played(matchs_joues, joueur1, joueur2):
                i += 1
                joueur2 = joueurs_tries[i + 1] if i + 1 < len(joueurs_tries) else None

            matchs_futurs.append([[joueur1, 0], [joueur2, 0]])
            joueurs_tries.remove(joueur1)
            joueurs_tries.remove(joueur2)
        return matchs_futurs

    def get_match_joues(self, id_tournoi):
        """Récupère la liste des matchs déjà joués d'un tournoi donné"""
        tournoi_en_cours = self.table.search((Query().ID == id_tournoi))
        matchs_deja_joues = []
        round_en_cours = int(tournoi_en_cours[0]["Tour actuel"])

        for i in range(1, round_en_cours + 1):
            matchs = tournoi_en_cours[0]["Tours"]["Round " + str(i)]["Matchs"]
            for j in range(1, len(matchs) + 1):
                matchs_deja_joues.append(matchs[j - 1])

        return matchs_deja_joues

    def get_tournament_ids(self):
        """Récupère les IDs de tous les tournois enregistrés dans la base de données"""
        tournois = self.db.table("_default").all()
        IDs = []
        for tournoi in tournois:
            IDs.append(
                tournoi["ID"],
            )
        return IDs
