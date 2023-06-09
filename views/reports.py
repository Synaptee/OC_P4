from tabulate import tabulate


class Affichage:
    @staticmethod
    def afficher_liste_joueurs(liste_joueurs: list):
        """Fonction qui affiche la liste des joueurs, par ordre alphabétique"""
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
        """Fonction qui affiche la liste des tournois, avec leur statut (en cours ou terminé)"""
        print("\n Liste des tournois : ")
        donnees_tournois = []
        for tournoi in liste_tournois:
            if tournoi.tour_actuel == tournoi.nombre_de_tours:
                statut = "Terminé"
            else:
                statut = "En cours"
            donnees_tournois.append(
                [
                    tournoi.ID,
                    tournoi.nom,
                    tournoi.lieu,
                    statut,
                ]
            )
        tableau = tabulate(
            donnees_tournois,
            headers=[
                "ID",
                "Nom",
                "Lieu",
                "Statut",
            ],
            tablefmt="fancy_grid",
        )
        print(tableau)

    @staticmethod
    def afficher_infos_tournois(infos_tournois: list):
        """Fonction qui affiche les informations d'un tournoi donné : date de début et nom"""
        print("\n Nom et date du tournoi demandé : ")
        tournoi = []
        infos = [
            infos_tournois[0]["Nom"],
            infos_tournois[0]["Date de début"],
            infos_tournois[0]["Date de fin"],
        ]
        tournoi.append(infos)
        tableau = tabulate(
            tournoi,
            headers=["Nom", "Date de début", "Date de fin"],
            tablefmt="fancy_grid",
        )
        print(tableau)

    @staticmethod
    def afficher_liste_joueurs_tournoi(infos_tournois: list):
        """Fonction qui affiche la liste des joueurs d'un tournoi donné, par ordre alphabétique"""
        print("\n Liste des joueurs du tournoi : ")

        infos = sorted([infos_tournois[0]["Joueurs"]][0])
        liste_joueurs = []
        for joueur in infos:
            liste_joueurs.append([joueur])

        tableau = tabulate(liste_joueurs, headers=["Joueurs"], tablefmt="fancy_grid")
        print(tableau)

    @staticmethod
    def afficher_rounds_matchs_tournois(rounds: dict):
        """Fonction qui affiche tous les rounds et les matchs d'un tournoi donné"""
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
