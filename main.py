import sqlite3

#conectando
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

#Criando a Tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS  livros (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,        
    autor TEXT NOT NULL,  
    ano INTEGER,    
    disponivel TEXT     
    )
""")
conexao.commit()
conexao.close()