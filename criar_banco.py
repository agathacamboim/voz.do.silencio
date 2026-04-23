import sqlite3

conn = sqlite3.connect('site.db')
cursor = conn.cursor()

# tabela de usuario
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT NOT NULL,
senha TEXT NOT NULL
)
""")

# tabela de relatos
cursor.execute("""
CREATE TABLE IF NOT EXISTS relatos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
texto TEXT,
nome TEXT
)
""")

# comentários
cursor.execute('''
CREATE TABLE IF NOT EXISTS comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    relato_id INTEGER,
    texto TEXT
)
''')

conn.commit()
conn.close()

