import random
from tinydb import TinyDB, Query
from modele.joueur import Joueur
from pathlib2 import Path

base_dir = Path(__file__).resolve().parent
db_path = base_dir / "database" / "tournois.json"


db = TinyDB(db_path)
table = db.table("_default")
tournois = table.all()
# Récupérer la liste des rounds en cours
id_tournoi = input("Saisissez l'ID du tournoi : ")

tournoi_en_cours = table.search((Query().ID == id_tournoi))
joueurs = tournoi_en_cours[0]["Joueurs"]


def get_match_joues(id_tournoi):
    tournoi_en_cours = table.search((Query().ID == id_tournoi))
    matchs_deja_joues = []
    round_en_cours = int(tournoi_en_cours[0]["Tour actuel"])

    for i in range(1, round_en_cours + 1):
        matchs_deja_joues.append(
            tournoi_en_cours[0]["Tours"]["Round " + str(round_en_cours)]["Matchs"][0]
        )

    return matchs_deja_joues


print(get_match_joues(id_tournoi))

round_en_cours = tournoi_en_cours[0]["Tour actuel"]
matchs_en_cours = get_match_joues(id_tournoi)


def already_played(matchs_en_cours, joueur1, joueur2):
    for match in matchs_en_cours:
        # print(f"Le match est : {match}")
        if (joueur1 in match[0] or joueur1 in match[1]) and (
            joueur2 in match[0] or joueur2 in match[1]
        ):
            print(f"{joueur1} et {joueur2} ont déjà joué ensemble")

            return True
    print(f"{joueur1} et {joueur2} n'ont pas encore joué ensemble")
    return False


def organiser_matchs(joueurs, matchs_joues):
    matchs_futurs = []
    joueurs_points = {}

    # Calcul des points de chaque joueur
    for joueur in joueurs:
        points = 0
        for match in matchs_joues:
            # print("BANCO")
            if match[0][0] == joueur:
                points += match[0][1]
            elif match[1][0] == joueur:
                points += match[1][1]
                # print(points)  # Récupération du score du joueur dans le match
        joueurs_points[joueur] = points

    # print(joueurs_points)

    # Tri des joueurs par points (du plus élevé au plus bas)
    joueurs_tries = sorted(joueurs, key=lambda x: joueurs_points[x], reverse=True)
    print(joueurs_tries)
    # return joueurs_tries

    while len(joueurs_tries) != 0:
        # for i in range(0, len(joueurs_tries)):
        i = 0
        joueur1 = joueurs_tries[i]
        joueur2 = joueurs_tries[i + 1] if i + 1 < len(joueurs_tries) else None

        while joueur2 and already_played(matchs_joues, joueur1, joueur2):
            i += 1
            joueur2 = joueurs_tries[i + 1] if i + 1 < len(joueurs_tries) else None

        matchs_futurs.append([[joueur1, 0], [joueur2, 0]])
        joueurs_tries.remove(joueur1)
        joueurs_tries.remove(joueur2)
        print(f"La liste des joueurs triés est : {joueurs_tries}")
    return matchs_futurs


datas = organiser_matchs(joueurs, matchs_en_cours)
print(datas)


# def ont_joue(joueur1, joueur2, liste_resultats):
#     for match in liste_resultats:
#         if (joueur1 in match[0] or joueur1 in match[1]) and (joueur2 in match[0] or joueur2 in match[1]):
#             return True
#     return False


# # Liste des matchs
# liste_resultats = [
#     [["Watson Emma", 1], ["Vachier-Lagrave Maxime", 1]],
#     [["Bern Stéphane", 0.5], ["Lamas Lorenzo", 0.5]],
#     [["Vachier-Lagrave Maxime", 1], ["Lamas Lorenzo", 0]],
#     [["Watson Emma", 0], ["Bern Stéphane", 1]],
# ]

# # Vérification
# joueur1 = "Watson Emma"
# joueur2 = "Lamas Lorenzo"
# if ont_joue(joueur1, joueur2, liste_resultats):
#     print(f"{joueur1} et {joueur2} se sont déjà affrontés.")
# else:
#     print(f"{joueur1} et {joueur2} ne se sont pas encore affrontés.")
