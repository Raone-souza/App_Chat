import pymysql

class ConexaoDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None  
        self.cursor = None   

    def conectar(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conexao.cursor()
            print("Conexão realizada com sucesso!")
        except pymysql.MySQLError as e:
            print(f"Erro ao conectar: {e}")

    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada com sucesso!")

# Criando a instância da classe ConexaoDB
conexao_db = ConexaoDB(
    host='localhost',
    user='root',
    password='raone199807',
    database='chat_db'
)

# Estabelecendo conexão antes de usar
conexao_db.conectar()
