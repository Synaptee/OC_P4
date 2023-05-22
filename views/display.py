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
