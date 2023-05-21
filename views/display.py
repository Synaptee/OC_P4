

class Affichage:
    def afficher_liste_joueurs(self, liste_joueurs):
        print("\n Liste des joueurs : ")
        for joueur in liste_joueurs:
            print(f'- {joueur.nom} {joueur.prenom}')
