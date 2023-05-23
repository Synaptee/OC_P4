from views.menu import MenuView
from controllers.joueur import ControllerJoueur
from controllers.tournois import ControllerTournoi
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
            self.menu_tournoi()
        elif choix == "3":
            self.display_tournois()
            tournoi = input("\n Saisissez l'ID du tournoi sélectionné' : ")
        elif choix == "4":
            self.menu_rapports()
        else:
            print("Option non disponible")

    def menu_rapports(self):
        MenuView.afficher_menu_rapports()
        choix = input("Saisissez votre choix : ")
        if choix == "1":
            display = ControllerJoueur()
            display.charger_joueurs()
            display.afficher_liste_joueurs()
            self.menu_rapports()
        elif choix == "2":
            self.display_tournois()
            self.menu_rapports()
        elif choix == "3":
            id_tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
            ControllerTournoi.get_tournoi(id_tournoi)
            self.menu_rapports()
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

    def menu_tournoi(self):
        MenuView.afficher_menu_tournoi()
        choix = input("Saisissez votre choix : ")
        if choix == "1":
            print("Ajouter un joueur")
        elif choix == "2":
            print("Sélectionner des joueurs dans la liste")
        elif choix == "3":
            self.display_tournois()
            tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
        elif choix == "4":
            print("Saisir les résultats du round")
        elif choix == "5":
            print("Afficher le classement")
        elif choix == "6":
            self.menu_principal()
        elif choix == "7":
            print("Fin du programme")

        else:
            print("Option non disponible")


    def display_tournois(self):
        display = ControllerTournoi()
        display.charger_tournois()
        display.afficher_liste_tournois()