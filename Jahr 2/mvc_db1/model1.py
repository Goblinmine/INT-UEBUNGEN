import mysql.connector          # Treiber importieren

class Db_Zugriff:

    def __init__(self):
        self.dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'root',
            'database': 'biblio',
            'port': '8889'}

        self.conn = mysql.connector.connect(**self.dbconfig)  # ** bedeutet, dass die Einzelwerte verwendet werden
        self.cursor = self.conn.cursor()


    def describeLeser(self):
        _SQL = "describe leser"
        self.cursor.execute(_SQL)
        result = self.cursor.fetchall()

        return result


    def insertBuch(self, id, sachgebiet, autor, titel, ort, jahr, verlag):
        _SQL = """insert into buecher 
                (BuchNr, Sachgebiet, Autor, Titel, Ort, Jahr, Verlag) 
                values 
                (%s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(_SQL, (id, sachgebiet, autor, titel, ort, jahr, verlag))
        self.conn.commit()
        return self.cursor.rowcount


    def get_all_Buecher(self):
        _SQL = """select * from buecher"""
        self.cursor.execute(_SQL)
        return self.cursor.fetchall()

    def delete_buchnr_from_Buecher(self, number):
        _SQL = "delete from buecher where buchnr=" + str(number)
        self.cursor.execute(_SQL)
        self.conn.commit()
        print(self.cursor.rowcount, "record(s) deleted")

    def get_next_buchnr(self):
        _SQL = "select max(buchnr) from buecher"
        self.cursor.execute(_SQL)
        next = self.cursor.fetchone()[0] + 1
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
    print(db.insertBuch('1606', 'Jugend', 'Cornelia Funke', 'Drachenreiter', 'Hamburg', '1997', 'Dressler'))
    #db.delete_buchnr_from_Buecher(1606)
    #for row in db.get_all_Buecher():
    #    print(row)

    #print(db.get_next_buchnr())


    db.close_db_Connection()


if __name__ == '__main__':
    testIt()