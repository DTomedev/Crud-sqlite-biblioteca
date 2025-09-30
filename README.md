# 📚 Sistema de Gerenciamento de Biblioteca  

Este projeto é um sistema simples de **gerenciamento de livros** utilizando **Python** e **SQLite3**.  
Permite realizar operações básicas de CRUD (Create, Read, Update e Delete), como cadastrar, listar, atualizar disponibilidade e remover livros.  

---

## 🚀 Funcionalidades  

- **Listar Livros** – Exibe todos os livros cadastrados no banco de dados.  
- **Cadastrar Livro** – Permite adicionar novos livros informando título, autor e ano.  
- **Atualizar Disponibilidade** – Altera o status de um livro entre disponível (`Sim`) ou indisponível (`Não`).  
- **Remover Livro** – Exclui um livro cadastrado a partir do seu ID.  
- **Banco de Dados Persistente** – Todos os dados ficam armazenados em `biblioteca.db`.  

---

## 🛠️ Tecnologias Utilizadas  

- **Python 3.x**  
- **SQLite3** (banco de dados embutido)  

---

## 📂 Estrutura do Projeto  

biblioteca/
│── main.py # Código principal do sistema
│── biblioteca.db # Banco de dados SQLite (gerado automaticamente)
└── README.md # Documentação do projeto

yaml
Copiar código

---

## ⚙️ Como Executar  

1. Clone este repositório ou copie o código para sua máquina:  
   ```bash
   git clone https://github.com/seuusuario/biblioteca.git
   cd main
   
  📌 Melhorias Futuras

Interface gráfica (Tkinter, PyQt ou Streamlit)

Pesquisa de livros por título ou autor

Relatórios de livros disponíveis e emprestados

Registro de empréstimos de usuários

👨‍💻 Autor

📌 Desenvolvido por Davi P. Tomé
