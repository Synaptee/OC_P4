class MenuView:
    def __init__(self):
        pass

    @staticmethod
    def afficher_titre_principal():
        print("   ***   Gestionnaire de tournois d'echecs   ***   ")
        print("Bienvenue dans le gestionnaire de tournois d'échecs")

    @staticmethod
    def afficher_menu():
        print("\n * Menu principal * \n")
        print("[1] Ajouter un joueur")
        print("[2] Créer un tournoi")
        print("[3] Menu tournoi")
        print("[4] Voir la liste des rapports")
        print("[5] Quitter l'application \n")

    @staticmethod
    def afficher_menu_rapports():
        print("\n * Rapports * \n")
        print("[1] Liste des joueurs par ordre aplhabétique")
        print("[2] Liste de tous les tournois")
        print("[3] Nom et date d'un tournoi donné")
        print("[4] Liste des joueurs d'un tournoi donné par ordre alphabétique")
        print("[5] Liste de tous les tours du tournoi et de tous les matchs du tour")
        print("[6] Revenir au menu principal")
        print("[7] Quitter l'application \n")

    @staticmethod
    def afficher_menu_tournoi():
        print("\n * Tournoi * \n")
        print("[1] Sélectionner des joueurs dans la liste")
        print("[2] Lancer le prochain round")
        print("[3] Reprendre le tournoi")
        print("[4] Saisir les résultats du round")
        print("[5] Revenir au menu principal")
        print("[6] Quitter l'application \n")
