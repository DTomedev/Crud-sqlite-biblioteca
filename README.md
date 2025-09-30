📚 Sistema de Gerenciamento de Biblioteca (SQLite + Python)

Este projeto é um sistema simples de gerenciamento de biblioteca desenvolvido em Python utilizando o banco de dados SQLite.
Ele permite cadastrar, listar, atualizar disponibilidade e remover livros diretamente via terminal.

🚀 Funcionalidades

Cadastrar livros: insere novos registros no banco de dados (titulo, autor, ano, disponível).

Listar livros: exibe todos os livros cadastrados com suas informações.

Atualizar disponibilidade: alterna a disponibilidade de um livro (Sim / Não).

Remover livros: exclui um livro do banco de dados pelo seu ID.

Menu interativo: interface de linha de comando para escolher as opções.

🗂 Estrutura da Tabela

A tabela criada no SQLite é:

CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
);

📦 Requisitos

Python 3.x instalado

Biblioteca sqlite3 (já inclusa no Python padrão, não é necessário instalar)
