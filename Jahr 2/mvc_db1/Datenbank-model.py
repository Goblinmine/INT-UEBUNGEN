import mysql.connector
import sys
import json

class db_Zugriff():
    dbconfig = {}
    conn = None
    cursor = None

    def __init__(self):
        try:
            self.dbconfig = None
            with open('.dbSecret.json') as f:
                self.dbconfig = json.load(f)

            self.conn = mysql.connector.connect(**self.dbconfig)  ## ** bedeutet, dass die Einzelwerte verwendet werden

            self.cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print("An error has occurred. {}".format(err))
            sys.exit()

        except:
            print("An error has occurred.")
            sys.exit()


    def describeLeser(self):
        _SQL = """describe leser"""
        res = None

        try:
            self.cursor.execute(_SQL)

            res = self.cursor.fetchall()

        except mysql.connector.DataError as err:
            print(err.msg)

        except mysql.connector.DatabaseError as err:
            print(err.msg)

        except mysql.connector.Error as err:
            print(err.msg)

        except:
            print("An error has occurred.")

        return res


    def insertBuch(self, buchnr, sachgebiet, autor, titel, ort, jahr, verlag):
        _SQL = """insert into buecher (buchnr, Sachgebiet, autor, titel, ort, jahr, verlag)
                    values (%s, %s, %s, %s, %s, %s, %s)"""
        try:
            self.cursor.execute(_SQL, [buchnr, sachgebiet, autor, titel, ort, str(jahr), verlag])
            self.conn.commit()
            return self.cursor.rowcount

        except mysql.connector.DataError as err:
            print(err.msg)

        except mysql.connector.IntegrityError as err:
            print(err.msg)

        except mysql.connector.DatabaseError as err:
            print(err.msg)

        except mysql.connector.Error as err:
            print(err.msg)

        except:
            print("An error has occurred.")


    def get_all_Buecher(self):
        _SQL = """select * from buecher"""
        res = None

        try:
            self.cursor.execute(_SQL)
            res = self.cursor.fetchall()

        except mysql.connector.DataError as err:
            print(err.msg)

        except mysql.connector.DatabaseError as err:
            print(err.msg)

        except mysql.connector.Error as err:
            print(err.msg)

        except:
            print("An error has occurred.")

        return res


    def close_db_Connection(self):
        try:
            self.cursor.close()
            self.conn.close()

        except mysql.connector.InternalError as err:
            print(err.msg)


    def delete_buchnr_from_Buecher(self, number):
        _SQL = """delete from buecher where buchnr = """ + str(number)

        try:
            self.cursor.execute(_SQL)
            self.conn.commit()
            print(self.cursor.rowcount, "record(s) deleted")

        except mysql.connector.DataError as err:
            print(err.msg)

        except mysql.connector.DatabaseError as err:
            print(err.msg)

        except mysql.connector.Error as err:
            print(err.msg)

        except:
            print("An error has occurred.")

def testIt():
    db_access = db_Zugriff()
    #res = db_access.describeLeser()
    #if res != None:
    #    for i in res:
    #        print(i)

    #print("Alle Bücher")
    rows = db_access.insertBuch("1608", "Jugend", "Cornelia Funke", "Drachenreiter", "Hamburg", 1997, "Dressler")
    print(str(rows), 'Rows affected')
    #db_access.delete_buchnr_from_Buecher(1608)

    #buecher = db_access.get_all_Buecher()

    #if buecher != None:
    #    for buch in buecher:
    #        print(buch)

    db_access.close_db_Connection()


testIt()