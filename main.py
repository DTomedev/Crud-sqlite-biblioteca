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

#Funções

#Cadastrando livros
def cadastrar_livro():
    try:
        titulo_livro = input("Digite o titulo do livro: ").strip().lower()
        autor_livro = input("Digite o autor do livro: ").strip().lower()
        while True:  
            try:
                ano_livro = int(input("Digite o ano de lançamento do livro: "))
                break
            except ValueError:
                print("Por favor, Digite um número válido.⚠️")

        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?,"Sim")
        """, (titulo_livro, autor_livro, ano_livro))

        conexao.commit()
        print("Livro Cadastrado com sucesso!✔")

    except Exception as erro:
        print("Erro ao cadastrar livro!⚠️")

#