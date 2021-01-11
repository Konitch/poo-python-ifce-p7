import sqlite3

class Info():
    def __init__(self):
        self.conectar = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conectar.cursor()
        
        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement,
                     aluno text,
                     idade integer,
                     email text,
                     curso text,
                     senha text)""")
        self.conectar.commit()
        c.close()