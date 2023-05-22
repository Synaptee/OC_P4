from views.menu import MenuView
from controllers.joueur import Display
from modele.joueur import Joueur


class Menu:
    def __init__(self):
        pass

    def menu_principal(self):
        MenuView.afficher_titre_principal()
        MenuView.afficher_menu()
        choix = input('Saisissez votre choix : ')
        if choix == "1":

            nom = input("Saisissez le nom du joueur : ")
            prenom = input("Saisissez le prénom du joueur : ")
            date_de_naissance = input("Saisissez la date de naissance du joueur : ")
            id_national = input("Saisissez l'ID national du joueur : ")
            Joueur.ajouter_joueur(nom, prenom, date_de_naissance, id_national)
            self.menu_principal()

        elif choix == "4":
            self.menu_rapports()
        else:
            print("Option non disponible")

    def menu_rapports(self):
        MenuView.afficher_menu_rapports()
        choix = input("Saisissez votre choix : ")
        if choix == "1":
            display = Display()
            display.charger_joueurs()
            display.afficher_liste_joueurs()
            self.menu_rapports()
        elif choix == "2":
            print("Liste de tous les tournois")
        elif choix == "3":
            print("Nom et date d'un tournoi donné")
        elif choix == "4":
            print("Liste des joueurs d'un tournoi donné par ordre alphabétique")
        elif choix == "5":
            print("Liste de tous les tours du tournoi et de tous les matchs du tour")
        elif choix == "6":
            self.menu_principal()
        elif choix == "7":
            print("Fin du programme")

        else:
            print("Option non disponible")
