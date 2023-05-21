from tinydb import TinyDB
from pathlib2 import Path


base_dir = Path(__file__).resolve().parent.parent
db_path = db_path = base_dir / 'database' / 'chess_mgt.json'

class Joueur:
    def __init__(self,nom, prenom, date_de_naissance, id_national):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.id_national = id_national

    @staticmethod
    def ajouter_joueur(nom, prenom, date_de_naissance, id_national):
        db = TinyDB(db_path)
        table = db.table('_default')
        table.insert({'Nom': nom, 'Prénom': prenom, 'Date de naissance': date_de_naissance, 'ID': id_national})



