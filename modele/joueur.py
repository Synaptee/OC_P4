from tinydb import TinyDB, Query
from pathlib2 import Path


base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / "database" / "joueurs.json"


class Joueur:

    db = TinyDB(db_path)
    table = db.table("_default")
    
    def __init__(self, nom:str="", prenom:str="", date_de_naissance:str="", id_national:str=""):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.id_national = id_national
      

   
    def ajouter_joueur(self):
        """Fonction qui ajoute un joueur au fichier si le joueur n'existe pas déjà"""
        if not self.verification_existence_joueur():
            self.update_joueur_db()
            print("Joueur ajouté à la base de données")
       
    
    def verification_existence_joueur(self):
        """Fonction qui vérifie si un joueur existe déjà dans la base, grâce à son ID"""
        query = self.table.search((Query().ID == self.id_national))
        if query:
            print("\n Le joueur existe déjà dans la base de données \n")
            return True
        else:
            print("Le joueur n'existe pas dans la base de données")
            return False
        
    def update_joueur_db(self):
        """Fonction qui permet de charger les données du joueur dans le fichier de JSON"""
        self.table.insert(
                {
                    "Nom": self.nom,
                    "Prénom": self.prenom,
                    "Date de naissance": self.date_de_naissance,
                    "ID": self.id_national,
                }
            )
