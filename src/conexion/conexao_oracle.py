import oracledb
import sys
from pandas import DataFrame

class ConexaoOracle:
    def __init__(self, can_write:bool=False):
        self.can_write = can_write
        self.host = ""
        self.cur = None
        self.conn = None
        self.port = None
        self.service_name = ""
    
        try:
            with open("src/conexion/acesso/autenticacao.oracle", "r") as f:
                self.host, self.port, self.service_name, self.user, self.senha = f.read().split(",")
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

    # select
    def sqlToTuple(self, query:str):
        try:
            self.cur.execute(query)
            row = self.cur.fetchone() 
            return row 
        except oracledb.DatabaseError as e:
            print(e)
            return None

    # insert and return id
    def return_id(self, query:str, params:tuple):
        try:
            id = self.cur.var(int)
            all_params = params + (id,)
            self.cur.execute(query, all_params)
            self.conn.commit()
            return id.getvalue()[0]
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
    
    def sqlToDataFrame(self, query:str) -> DataFrame:
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return DataFrame(rows, columns=[col[0].lower() for col in self.cur.description])