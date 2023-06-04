from tabulate import tabulate


class Affichage:
    @staticmethod
    def afficher_liste_joueurs(liste_joueurs: list):
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
                "Tours actuel",
                "Description",
            ],
            tablefmt="fancy_grid",
        )
        print(tableau)

    @staticmethod
    def afficher_infos_tournois(infos_tournois: list):
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
        print("\n Liste des joueurs du tournoi : ")

        infos = sorted([infos_tournois[0]["Joueurs"]][0])
        print(infos)
        liste_joueurs = []
        for joueur in infos:
            liste_joueurs.append([joueur])

        tableau = tabulate(liste_joueurs, headers=["Joueurs"], tablefmt="fancy_grid")
        print(tableau)
