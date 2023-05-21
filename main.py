from tinydb import TinyDB, Query
import os
from controllers.menu import Menu




def check_bdd_exists():
    """Fonction qui vérifie si la base de données existe, si elle n'existe pas elle la crée, et renvoie la base de données"""
    if os.path.exists("chess_mgt.json"):
        db = TinyDB('chess_mgt.json')
        return db
    else:
        db = TinyDB('chess_mgt.json')
        joueurs = db.table("joueurs")
        tournois = db.table("tournois")
        return db


def main():
    print("Début d'exécution du programme")
    menu = Menu()
    menu.menu_principal()





if __name__ == "__main__":
    main()
    print("Fin d'exécution du programme \n")

   