from tinydb import TinyDB, Query
from pathlib2 import Path


base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / 'database' / 'joueurs.json'


class Joueur:
    def __init__(self, nom, prenom, date_de_naissance, id_national):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.id_national = id_national

    @staticmethod
    def ajouter_joueur(nom, prenom, date_de_naissance, id_national):
        db = TinyDB(db_path)
        table = db.table('_default')
        if not Joueur.verification_existence_joueur(id_national):
            table.insert({'Nom': nom, 'Prénom': prenom, 'Date de naissance': date_de_naissance, 'ID': id_national})
            print("Joueur ajouté à la base de données")

    @staticmethod
    def verification_existence_joueur(id_national):
        db = TinyDB(db_path)
        table = db.table('_default')
        query = table.search((Query().ID == id_national))
        if query:
            print("\n Le joueur existe déjà dans la base de données \n")
            return True
        else:
            print("Le joueur n'existe pas dans la base de données")
            return False
