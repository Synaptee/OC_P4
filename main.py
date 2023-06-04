from tinydb import TinyDB
import os
from controllers.menu import Menu
from pathlib2 import Path


def check_bdd_exists():
    """Function that check if database already exists, and if not, creates the database"""
    base_dir = Path(__file__).resolve().parent
    joueurs_path = base_dir / "database" / "joueurs.json"
    tournois_path = base_dir / "database" / "tournois.json"
    if not os.path.exists(joueurs_path):
        db = TinyDB(joueurs_path)
        db.close()
    if not os.path.exists(tournois_path):
        db = TinyDB(tournois_path)
        db.close()


def main():
    check_bdd_exists()
    menu = Menu()
    menu.menu_principal()


if __name__ == "__main__":
    main()
    print("Fin d'exécution du programme \n")
