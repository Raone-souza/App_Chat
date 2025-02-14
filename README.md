# Chat Local multiusuário com Python

Este é um aplicativo desenvolvido em Python com a biblioteca CustomTkinter, projetado para facilitar a troca de mensagens em tempo real dentro de uma rede local.  O sistema é composto por um cliente e um servidor, permitindo que múltiplos usuários se conectem e se comuniquem de forma eficiente.


## Funcionalidades

### 1. **CRUD Parcial**
Implementei um **CRUD básico** (Create, Read, Update, Delete) para a gestão de usuários. Com isso, agora é possível cadastrar, visualizar e manipular dados de forma eficiente, melhorando a usabilidade e a organização do sistema.

### 2. **Banco de Dados Integrado**
O sistema agora armazena dados de **login e cadastro** de usuários em um banco de dados local, garantindo maior segurança e praticidade no gerenciamento dessas informações. O uso do banco de dados facilita a manutenção e a escalabilidade do sistema.

### 3. **Validação de Dados de Login**
Implementei uma **consulta ao banco de dados** para validar as credenciais dos usuários durante o processo de login. Isso oferece uma **autenticação mais confiável** e aumenta a segurança do sistema, evitando acessos indevidos.

### 4. **Automação com Subprocess**
Utilizei a biblioteca **subprocess** para **iniciar o servidor automaticamente**, facilitando o processo de execução do sistema sem a necessidade de iniciar manualmente o servidor, tornando o ambiente de desenvolvimento mais ágil.

### 5. **Comunicação em Tempo Real com Sockets e Threading**
A comunicação entre o **servidor e os clientes** agora utiliza **sockets e threading**, permitindo uma **interação rápida e em tempo real**. Isso proporciona uma experiência de uso mais dinâmica, com mensagens sendo enviadas e recebidas instantaneamente.

### 6. **Melhorias de Design**
A interface gráfica foi **reformulada e otimizada**, tornando o sistema **mais moderno, intuitivo e visualmente atraente**. Com isso, a experiência do usuário foi significativamente aprimorada, tornando o uso do aplicativo mais agradável.

### 7. **Melhorias de Performance**
O sistema está agora mais rápido e fluido, com **otimizações no fluxo de dados e navegação**, o que garante uma performance mais eficiente e uma resposta mais ágil, especialmente em operações mais intensivas.


## Tecnologias Utilizadas

- Sockets e Threading: Para implementar comunicação em tempo real, permitindo uma interação rápida e eficaz entre o servidor e os clientes.

- CustomTkinter: Utilizada para criar uma interface gráfica intuitiva e moderna.

- PyMySQL: Para integrar o sistema com o banco de dados MySQL, facilitando o armazenamento e a consulta dos dados de login e cadastro.

- Subprocess: Utilizado para automatizar a execução do servidor, simplificando o processo de inicialização do sistema.

- OS: Para manipulação do sistema e execução de comandos diretamente do código Python, proporcionando mais controle e flexibilidade na execução.


## Como Executar o Projeto

### Pré-requisitos:
- Python 3.10 ou superior instalado.

### Instalar as dependências do projeto:

`pip install -r requirements.txt`

### Executando o Cliente:

- Navegue até a pasta do projeto.
Execute o arquivo da interface gráfica:

`python App.py`



## Contribuições

Contribuições são bem-vindas!
Se você deseja contribuir, por favor, abra um pull request ou entre em contato pelo e-mail acima.


## Contato

**Caso tenha interesse ou dúvidas sobre o projeto, entre em contato comigo:**

- E-mail: raone199807@gmail.com
- LinkedIn: https://www.linkedin.com/in/raonesouza/
- GitHub: https://github.com/Raone-souza
