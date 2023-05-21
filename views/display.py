from tabulate import tabulate

class Affichage:
    def afficher_liste_joueurs(self, liste_joueurs):
        print("\n Liste des joueurs : ")
        donnees_joueurs = []
        #donnees_joueurs = [[joueur['Nom'], joueur['Prénom'], joueur['Date de naissance'], joueur['ID']] for joueur in liste_joueurs]
        
        for joueur in liste_joueurs:
            donnees_joueurs.append([joueur.nom, joueur.prenom])
        #     print(f'- {joueur.nom} {joueur.prenom}')
        tableau = tabulate(donnees_joueurs, headers=["Nom", "Prénom"], tablefmt="fancy_grid")
        print(tableau)

