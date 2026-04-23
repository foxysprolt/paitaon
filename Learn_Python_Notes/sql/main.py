import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS primeira_table(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE)


               """)

cursor.execute(""" INSERT INTO primeira_table
                (nome, saldo, cpf) VALUES
                ('Rafael', 163854354, '654681354')
                """)


conexao.commit()
