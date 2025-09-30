📚 Sistema de Gerenciamento de Biblioteca

Este projeto é um sistema simples de gerenciamento de livros utilizando Python e SQLite3.
Permite realizar operações básicas de CRUD (Create, Read, Update e Delete), como cadastrar, listar, atualizar disponibilidade e remover livros.

🚀 Funcionalidades

✔ Listar Livros – Exibe todos os livros cadastrados no banco de dados.
✔ Cadastrar Livro – Permite adicionar novos livros informando título, autor e ano.
✔ Atualizar Disponibilidade – Altera o status de um livro entre disponível (Sim) ou indisponível (Não).
✔ Remover Livro – Exclui um livro cadastrado a partir do seu ID.
✔ Banco de Dados Persistente – Todos os dados ficam armazenados em biblioteca.db.

🛠️ Tecnologias Utilizadas

Python 3.x

SQLite3 (banco de dados embutido)

📂 Estrutura do Projeto
biblioteca/
│── biblioteca.py       # Código principal do sistema
│── biblioteca.db       # Banco de dados SQLite (gerado automaticamente)
└── README.md           # Documentação do projeto

⚙️ Como Executar

Clone este repositório ou copie o código para sua máquina:

git clone https://github.com/seuusuario/biblioteca.git
cd biblioteca


Execute o programa em Python:

python biblioteca.py


O menu será exibido no terminal:

------------------------------
BIBLIOTECA
1 - Listar livros
2 - Cadastrar Livro
3 - Atualizar Disponibilidade
4 - Remover Livro
5 - Sair
------------------------------
Escolha uma opção:

📖 Exemplo de Uso
✅ Listando Livros
ID 1 | TÍTULO: Dom Casmurro | AUTOR: Machado de Assis | ANO: 1899 | DISPONIBILIDADE: Sim
ID 2 | TÍTULO: O Pequeno Príncipe | AUTOR: Antoine de Saint-Exupéry | ANO: 1943 | DISPONIBILIDADE: Sim

✅ Cadastrando um Livro
Digite o título do livro: Capitães da Areia
Digite o autor do livro: Jorge Amado
Digite o ano de lançamento do livro: 1937
✔ Livro cadastrado com sucesso!

📌 Melhorias Futuras

🔹 Interface gráfica (Tkinter, PyQt ou Streamlit)
🔹 Pesquisa de livros por título ou autor
🔹 Relatórios de livros disponíveis e emprestados
🔹 Registro de empréstimos de usuários

👨‍💻 Autor

📌 Desenvolvido por [Seu Nome]
🔗 LinkedIn
 | GitHub
