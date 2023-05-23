from tinydb import TinyDB, Query


def test():
        db = TinyDB('/Users/jbstudio/Desktop/DA_Python/OC_P4/database/tournois.json')
        table = db.table('_default')
        query = table.search((Query().ID == "BLP2223"))
        print(query[0]['Nom'])

test()