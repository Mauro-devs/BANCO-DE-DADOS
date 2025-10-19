import oracledb
import sys

class ConexaoOracle:
    def __init__(self, can_write:bool=False):
        self.can_write = can_write
        self.host = ""
        self.port = None
        self.service_name = ""
    
        try:
            with open("connexion/acesso/autentificacao.oracle", "r") as f:
                self.user, self.senha = f.read().split(",")
        except FileNotFoundError:
            print("")
            print("")

    def __del__(self):
        if self.cur:
            self.close()

    def connect(self):
        try:
            dsn = oracledb.makedsn(host=self.host, port=self.port, service_name=self.service_name)
            self.conn = oracledb.connect(user=self.user, password=self.senha, dsn=dsn)
            self.cur = self.conn.cursor()
            return self.cur
        except oracledb.DatabaseError as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)

    def sqlToMatrix(self, query:str):
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return rows
        except oracledb.DatabaseError as e:
            print(e)
            return []

    def sqlToTuple(self, query:str):
        try:
            self.cur.execute(query)
            row = self.cur.fetchone() 
            return row 
        except oracledb.DatabaseError as e:
            print(e)
            return None

    def write(self, query:str):
        if not self.can_write:
            raise Exception("")
        
        try:
            self.cur.execute(query)
            self.conn.commit()
        except oracledb.DatabaseError as e:
            print()
            self.conn.rollback()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
