import mysql.connector
import json

conn = None
curser = None

def connect():
    global conn, curser
    dbconfig = None
    with open('.dbSecret.json') as f:
        dbconfig = json.load(f)
    conn = mysql.connector.connect(**dbconfig)
    curser = conn.cursor()
    
def main():
    global curser, conn
    connect()
    
    _SQL = "SELECT * FROM buecher;"
    curser.execute(_SQL)
    print(curser.fetchall())

main()