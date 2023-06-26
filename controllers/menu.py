from views.menu import MenuView
from controllers.joueur import ControllerJoueur
from controllers.tournois import ControllerTournoi
from modele.joueur import Joueur
from modele.tournois import Tournoi
from modele.rounds import Round
import datetime


class Menu:
    def __init__(self):
        pass

    def menu_principal(self):
        """Affiche le menu principal et les options disponibles"""
        MenuView.afficher_titre_principal()
        MenuView.afficher_menu()
        choix = input("Saisissez votre choix : ")
        if choix == "1":
            nom = input("Saisissez le nom du joueur : ")
            prenom = input("Saisissez le prénom du joueur : ")
            date_de_naissance = input("Saisissez la date de naissance du joueur : ")
            id_national = input("Saisissez l'ID national du joueur : ")
            joueur = Joueur(nom, prenom, date_de_naissance, id_national)
            joueur.ajouter_joueur()
            self.menu_principal()
        elif choix == "2":
            nom = input("Saisissez le nom du tournoi : ")
            lieu = input("Saisissez le lieu du tournoi : ")
            date = input("Saisissez la date de début du tournoi : ")
            date_fin = input("Saisissez la date de fin du tournoi : ")
            nombre_de_tours = input(
                "Saisissez le nombre de tours du tournoi (4 par défaut) : "
            )
            joueurs = []
            description = input("Saisissez une description du tournoi : ")
            tournoi = Tournoi(
                nom, lieu, date, date_fin, nombre_de_tours, 0, [], joueurs, description
            )
            tournoi.ajouter_tournoi()
            self.menu_tournoi()
        elif choix == "3":
            self.menu_tournoi()
        elif choix == "4":
            self.menu_rapports()
        elif choix == "5":
            pass
        else:
            print("Option non disponible")

    def menu_rapports(self):
        """Affiche le menu des rapports et les options disponibles"""
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
            if not self.check_id_tournoi(id_tournoi):
                self.menu_rapports()
            ControllerTournoi.get_tournoi(id_tournoi)
            self.menu_rapports()
        elif choix == "4":
            id_tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
            if not self.check_id_tournoi(id_tournoi):
                self.menu_rapports()

            ControllerTournoi.get_joueurs_tournoi(id_tournoi)
            self.menu_rapports()
        elif choix == "5":
            id_tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
            if not self.check_id_tournoi(id_tournoi):
                self.menu_rapports()
            datas_round = ControllerTournoi.search_tournoi(id_tournoi)
            datas_round = datas_round[0]["Tours"]
            ControllerTournoi.display_rounds_matchs_tournoi(datas_round)
            self.menu_rapports()
        elif choix == "6":
            self.menu_principal()
        elif choix == "7":
            print("Fin du programme")

        else:
            print("Option non disponible")

    def menu_tournoi(self):
        """Affiche le menu des tournois et les options disponibles"""
        MenuView.afficher_menu_tournoi()
        choix = input("Saisissez votre choix : ")
        if choix == "1":
            id_tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
            if not self.check_id_tournoi(id_tournoi):
                self.menu_tournoi()
            nb_joueurs = int(input("Saisissez le nombre de joueurs à sélectionner : "))
            display = ControllerJoueur()
            liste_joueurs_selectionnes = display.selectionner_joueurs(nb_joueurs)
            Tournoi.ajouter_liste_joueurs_au_tournoi(
                liste_joueurs_selectionnes, id_tournoi
            )
            print(
                f"Les joueurs {liste_joueurs_selectionnes} ont été ajoutés au tournoi"
            )
            self.menu_tournoi()

        elif choix == "2":
            id_tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
            if not self.check_id_tournoi(id_tournoi):
                self.menu_tournoi()
            datas = ControllerTournoi.search_tournoi(id_tournoi)
            current_round = str(datas[0]["Tour actuel"])
            joueurs = datas[0]["Joueurs"]
            nb_tours = datas[0]["Nombre de tours"]
            if current_round == str(nb_tours):
                print("Le dernier round de ce tournoi a déjà été lancé")
            else:
                if current_round == "0":
                    controller = ControllerTournoi()
                    if controller.check_if_players(id_tournoi):
                        controller.generate_random_matches(id_tournoi)
                        print("Round 1 généré et tournoi lancé")
                    else:
                        print(
                            "Le tournoi ne peut pas être lancé car aucun joueur n'a été ajouté"
                        )
                else:
                    controller = ControllerTournoi()
                    matchs_joues = controller.get_match_joues(id_tournoi)
                    new_matches = controller.organiser_matchs(joueurs, matchs_joues)
                    round = Round(
                        name="Round " + str(int(current_round) + 1),
                        matchs=new_matches,
                        start_date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                        tournament_id=id_tournoi,
                    )

                    round.save_new_round()
                    current_round = int(current_round) + 1
                    controller = ControllerTournoi()
                    controller.update_current_round(id_tournoi, current_round)
            self.menu_tournoi()

        elif choix == "3":
            tournoi = input("Saisissez l'ID du tournoi sélectionné' : ")
            if not self.check_id_tournoi(id_tournoi):
                self.menu_tournoi()
            datas_round = ControllerTournoi.get_current_round(tournoi)
            name_round = "Round " + str(datas_round[1])
            # print(f"Round en cours : {name_round}")
            matchs_round = datas_round[0]["Matchs"]
            # print(f"Matchs du round : {matchs_round}")
            round = Round(name=name_round, matchs=matchs_round)
            round.enter_round_results()
            round.save_round_results(tournoi)
            self.menu_tournoi()
        elif choix == "4":
            self.menu_principal()
        elif choix == "5":
            print("Fin du programme")

        else:
            print("Option non disponible")

    def display_tournois(self):
        display = ControllerTournoi()
        display.charger_tournois()
        display.afficher_liste_tournois()

    def check_id_tournoi(self, id_tournoi):
        check = ControllerTournoi()
        if not id_tournoi in check.get_tournament_ids():
            print("Cet ID n'existe pas")
        else:
            pass
