from tabulate import tabulate


class Affichage:
    @staticmethod
    def afficher_liste_joueurs(liste_joueurs: list):
        """Function that displays the list of players, by alphabetical order"""
        print("\n Liste des joueurs : ")
        donnees_joueurs = []

        for joueur in liste_joueurs:
            donnees_joueurs.append(
                [
                    joueur.nom,
                    joueur.prenom,
                    joueur.date_de_naissance,
                    joueur.id_national,
                ]
            )
        tableau = tabulate(
            donnees_joueurs,
            headers=["Nom", "Prénom", "Date de naissance", "ID"],
            tablefmt="fancy_grid",
        )
        print(tableau)

    @staticmethod
    def afficher_liste_tournois(liste_tournois: list):
        """Function that displays the list of tournaments, with their informations"""
        print("\n Liste des tournois : ")
        donnees_tournois = []
        for tournoi in liste_tournois:
            donnees_tournois.append(
                [
                    tournoi.ID,
                    tournoi.nom,
                    tournoi.lieu,
                    tournoi.date_debut,
                    tournoi.date_fin,
                    tournoi.nombre_de_tours,
                    len(tournoi.joueurs),
                    tournoi.tour_actuel,
                    tournoi.description,
                ]
            )
        tableau = tabulate(
            donnees_tournois,
            headers=[
                "ID",
                "Nom",
                "Lieu",
                "Date de début",
                "Date de fin",
                "Nb tours",
                "Nb joueurs inscrits",
                "Tours actuel",
                "Description",
            ],
            tablefmt="fancy_grid",
        )
        print(tableau)

    @staticmethod
    def afficher_infos_tournois(infos_tournois: list):
        """Function that displays the informations of a specified tournament : name and start date"""
        print("\n Nom et date du tournoi demandé : ")
        tournoi = []
        infos = [infos_tournois[0]["Nom"], infos_tournois[0]["Date de début"]]
        tournoi.append(infos)
        tableau = tabulate(
            tournoi, headers=["Nom", "Date de début"], tablefmt="fancy_grid"
        )
        print(tableau)

    @staticmethod
    def afficher_liste_joueurs_tournoi(infos_tournois: list):
        """Function that displays the list of players, for a specified tournament"""
        print("\n Liste des joueurs du tournoi : ")

        infos = sorted([infos_tournois[0]["Joueurs"]][0])
        print(infos)
        liste_joueurs = []
        for joueur in infos:
            liste_joueurs.append([joueur])

        tableau = tabulate(liste_joueurs, headers=["Joueurs"], tablefmt="fancy_grid")
        print(tableau)

    @staticmethod
    def afficher_rounds_matchs_tournois(rounds: dict):
        for round in rounds:
            print(f" \n ********** {round} ********** ")
            datas_round = []
            for match in rounds[round]["Matchs"]:
                infos = [match[0][0], match[1][0]]
                datas_round.append(infos)
                tableau = tabulate(
                    datas_round, headers=["Joueur 1", "Joueur 2"], tablefmt="fancy_grid"
                )
            print(tableau)
