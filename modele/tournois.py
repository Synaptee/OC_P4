from tinydb import TinyDB, Query
from pathlib2 import Path


base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / 'database' / 'tournois.json'


class Tournoi:
    db = TinyDB(db_path)
    table = db.table('_default')

    def __init__(self, nom, lieu, date_debut, date_fin, nombre_de_tours:4, tour_actuel:0, tours:list, joueurs, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_de_tours = nombre_de_tours
        self.tour_actuel = tour_actuel
        self.tours = int(tours)
        self.joueurs = joueurs
        self.description = description
        self.ID = (nom[0:2] + lieu[0] + date_debut[0:2] +date_debut[-2:]).upper()

    def ajouter_tournoi(self):
        self.table.insert({'Nom': self.nom, 'Lieu': self.lieu, 'Date de début': self.date_debut, 'Date de fin': self.date_fin,
                      'Nombre de tours': self.nombre_de_tours, 'Tour actuel': self.tour_actuel, 'Tours': self.tours,
                      'Joueurs': self.joueurs, 'Description': self.description, 'ID': self.ID})
        print("Tournoi ajouté à la base de données")

    



