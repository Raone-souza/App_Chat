## Sobre o Projeto

O Library Management System ( Sistema de Gerenciamento de Biblioteca ) é uma Web API desenvolvida para facilitar a gestão de livros, usuários e empréstimos em uma biblioteca. O sistema permite cadastro, consulta, edição e remoção de registros, proporcionando uma administração eficiente dos recursos da biblioteca.

## Tecnologias Utilizadas

- **Linguagem: C#**
- **Framework: .NET Core / .NET 6+**
- **Banco de Dados: SQL Server**
- **ORM: Entity Framework Core**
- **Documentação: Swagger**
- **Gerenciamento de Dependências: NuGet**

## Principais funcionalidades

- **Cadastro de livros, usuários e empréstimos.**
- **Consulta de livros disponíveis**
- **Documentação interativa via Swagger**


## Como Executar o Projeto

### 1. Configurar o Ambiente

`Instale o .NET SDK 6+`

`Instale o SQL Server e crie um banco de dados`

### 2. Rodar o Projeto

#### Clone este repositório:

`git clone https://github.com/Raone-souza/library-management-system.git`

### Navegue até a pasta do projeto:

`cd library-management-system`

### Configure a string de conexão no appsettings.json:

`"ConnectionStrings": {
   "DefaultConnection": "Server=SEU_SERVIDOR;Database=BibliotecaDB;Trusted_Connection=True;"
}`

### Aplique as migrações do banco de dados:

`dotnet ef database update`

### Execute a API:

`dotnet run`

### 3. Acessar a API

` Acesse a documentação no Swagger: http://localhost:5000/swagger`

### Contribuição

**Contribuições são bem-vindas! Para contribuir:**

- Faça um fork do projeto

- Crie uma branch: git checkout -b minha-feature

- Faça suas alterações e commit: git commit -m 'Nova funcionalidade'

- Envie para o repositório: git push origin minha-feature

- Abra um Pull Request
