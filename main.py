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

#tabela pré-definida
livros = [
    ("Dom Casmurro", "Machado de Assis", 1899, "Sim"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Sim"),
    ("A Hora da Estrela", "Clarice Lispector", 1977, "Sim"),
]

cursor.executemany("""
INSERT INTO livros (titulo, autor, ano, disponivel)
VALUES (?, ?, ?, ?)
""", livros)

conexao.commit()
