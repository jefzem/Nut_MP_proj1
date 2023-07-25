import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_Usagers(conn):
    """Lister la base usagers
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usagers ")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def Insert_Usagers(conn, nom, prenom, credit):
    """insere un usager
    """
    cur = conn.cursor()

    cur.execute("INSERT INTO usagers (nom, prenom, credit) VALUES (?, ?, ?)", (nom, prenom, credit))
    conn.commit()

def Modif_Credit_Usagers(conn, nom, valeur):
    """modifier le crédit d'un usager
    """
    cur = conn.cursor()

    cur.execute("UPDATE usagers SET credit = ? WHERE nom LIKE ?", (valeur, nom))
    conn.commit()


"programme principal"
def main():
    database = r".\PILCv0.5.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        nom='Jean'
        prenom='Dupont'
        credit=0
        #Insert_Usagers(conn, nom, prenom, credit)
        print("2. Query all tasks")
        select_all_Usagers(conn)
        nom ='%No%'
        valeur = 138
        Modif_Credit_Usagers(conn, nom, valeur)
        select_all_Usagers(conn)

if __name__ == '__main__':
    main()