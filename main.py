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
        while True:  #Loop para garantir que o ano seja um número inteiro
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

#Listar Livros
def listar_livros():
    try:
        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"ID {linha[0]} | TÍTULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIBILIDADE: {linha[4]}")
    except Exception as erro:
        print("Erro ao listar livros!⚠️")
    
#Atualização de Disponibilidade
def atualizar_disp():
    try:
        id_livro = int(input("Digite o ID do livro: "))
        # Verifica o status atual do livro
        cursor.execute("""
        SELECT disponivel FROM livros
        WHERE id = ?
        """, (id_livro,))
        resultado = cursor.fetchone() # pega uma única linha, em uma tupla ou None

        if resultado is None:
            print("⚠️ Livro não encontrado.")
            return
        disp_atual = resultado[0]
    
        if disp_atual == "Sim":
            nova_disp = "Não"   
        else:
            nova_disp = "Sim"

        while True:
            confirmar_alteracao = input("Digite 'confirmar' para alterar disponibilidade ou '0' para sair: ").lower()
            if confirmar_alteracao == "confirmar":
                cursor.execute("""
                UPDATE livros SET disponivel = ?
                WHERE id = ?  
                """, (nova_disp, id_livro))
                print(f"✔ Disponibilidade do livro {id_livro} alterada para: {nova_disp}")

            elif confirmar_alteracao == "0":
                break
            else: 
                print("Inválido!")
    except ValueError:
        print("⚠️ Digite um número válido para ID.")
    except Exception as erro:
        print("Erro ao atualizar disponibilidade: ", erro)

        conexao.commit()
        

#
