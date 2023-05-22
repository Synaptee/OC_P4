from views.menu import MenuView
from controllers.joueur import Display
from controllers.tournois import DisplayTournois
from modele.joueur import Joueur
from modele.tournois import Tournoi


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
        elif choix == "2":
            nom = input("Saisissez le nom du tournoi : ")
            lieu = input("Saisissez le lieu du tournoi : ")
            date = input("Saisissez la date de début du tournoi : ")
            date_fin = input("Saisissez la date de fin du tournoi : ")
            nombre_de_tours = input("Saisissez le nombre de tours du tournoi (4 par défaut) : ")
            joueurs = []
            description = input("Saisissez une description du tournoi : ")

            tournoi = Tournoi(nom, lieu, date, date_fin, nombre_de_tours, 0, [], joueurs, description)
            tournoi.ajouter_tournoi()
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
            display = DisplayTournois()
            display.charger_tournois()
            display.afficher_liste_tournois()
            self.menu_rapports()
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
