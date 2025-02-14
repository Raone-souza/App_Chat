import pymysql
from database.ConexaoDb import conexao_db

def cadastrar_usuario(nome_usuario, senha_usuario):
    if nome_usuario and senha_usuario:
        print(f"Usuário cadastrado: {nome_usuario}")
        print(f"Senha: {senha_usuario}")

        # Inserir no banco de dados
        sql = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
        valores = (nome_usuario, senha_usuario)

        try:
            # Usa o cursor da conexão existente para executar o SQL
            conexao_db.cursor.execute(sql, valores)
            conexao_db.conexao.commit()  # Commit para salvar as alterações
            print("Usuário cadastrado no banco de dados com sucesso!")
        except pymysql.MySQLError as e:
            print(f"Erro ao cadastrar usuário no banco de dados: {e}")
    else:
        print("Erro: Nome de usuário ou senha vazios!")
        