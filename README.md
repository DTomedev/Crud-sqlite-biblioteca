 📚 Sistema de Gerenciamento de Biblioteca

Um sistema simples de **gerenciamento de livros** feito em **Python + SQLite**.  
Permite cadastrar, listar, atualizar a disponibilidade e remover livros diretamente no terminal.

---

## ✨ Funcionalidades

- ➕ **Cadastrar livros**  
- 📋 **Listar livros cadastrados**  
- 🔄 **Atualizar disponibilidade** (`Sim` / `Não`)  
- 🗑 **Remover livros**  
- 🖥 **Menu interativo** no terminal  

---

## 🗂 Estrutura da Tabela

A tabela criada no SQLite segue o seguinte modelo:

```sql
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
);
⚙️ Requisitos
Python 3.x

Biblioteca sqlite3 (já vem instalada por padrão com o Python)

