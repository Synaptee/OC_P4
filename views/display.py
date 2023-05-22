from tabulate import tabulate


class Affichage:
    @staticmethod
    def afficher_liste_joueurs(liste_joueurs):
        print("\n Liste des joueurs : ")
        donnees_joueurs = []

        for joueur in liste_joueurs:
            donnees_joueurs.append([joueur.nom, joueur.prenom])
        #     print(f'- {joueur.nom} {joueur.prenom}')
        tableau = tabulate(donnees_joueurs, headers=["Nom", "Prénom"], tablefmt="fancy_grid")
        print(tableau)

    @staticmethod
    def afficher_liste_tournois(liste_tournois):
        print("\n Liste des tournois : ")
        donnees_tournois = []
        for tournoi in liste_tournois:
            donnees_tournois.append([tournoi.nom, tournoi.lieu, tournoi.date_debut, tournoi.date_fin, tournoi.nombre_de_tours, tournoi.tour_actuel, tournoi.description])
        tableau = tabulate(donnees_tournois, headers=["Nom", "Lieu", "Date de début", "Date de fin", "Nb tours", "Tours actuel", "Description"], tablefmt="fancy_grid")
        print(tableau)
