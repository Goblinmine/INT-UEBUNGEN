import mysql.connector          # Treiber importieren
import json

class Db_Zugriff:

    def __init__(self):
        self.dbconfig = None
        with open('.dbSecret.json') as f:
            self.dbconfig = json.load(f)

        self.conn = mysql.connector.connect(**self.dbconfig)  # ** bedeutet, dass die Einzelwerte verwendet werden
        self.cursor = self.conn.cursor()


    def describeLeser(self):
        _SQL = "describe leser"
        self.cursor.execute(_SQL)
        result = self.cursor.fetchall()

        return result


    def insertBuch(self, isbn, titel, author, auflage, preis):
        _SQL = """insert into buecher 
                (isbn, titel, autor, auflage, preis) 
                values 
                (%s, %s, %s, %s, %s)"""
        self.cursor.execute(_SQL, (isbn, titel, author, auflage, preis))
        self.conn.commit()
        return self.cursor.rowcount


    def get_all_Buecher(self):
        _SQL = """select * from buecher"""
        self.cursor.execute(_SQL)
        return self.cursor.fetchall()

    def delete_buchnr_from_Buecher(self, number):
        _SQL = "delete from buecher where isbn=" + str(number)
        self.cursor.execute(_SQL)
        self.conn.commit()
        print(self.cursor.rowcount, "record(s) deleted")

    def get_next_buchnr(self):
        _SQL = "select max(isbn) from buecher"
        self.cursor.execute(_SQL)
        next = int(self.cursor.fetchone()[0]) + 1
        return next


    def close_db_Connection(self):
        self.cursor.close()
        self.conn.close()


def testIt():
    db = Db_Zugriff()
    #res = db.describeLeser()
    #for row in res:
    #    print(row)

    #print("Alle Bücher")
    print(db.insertBuch(db.get_next_buchnr(), 'Drachenreiter', 'Cornelia Funke', '1', '10.5'))
    #db.delete_buchnr_from_Buecher(1606)
    #for row in db.get_all_Buecher():
    #    print(row)

    #print(db.get_next_buchnr())


    db.close_db_Connection()


if __name__ == '__main__':
    testIt()