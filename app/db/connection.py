import pymysql

class Connection:
    def __init__(self,host,port,user,password,db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def get_conn(self):
        try:
            return pymysql.connect(
                host=self.host,
               port=self.port,
               user=self.user,
               password=self.password,
                db=self.db)

        except pymysql.err.OperationalError as e :
            print(e)
            raise

conn = Connection("localhost",3306,"root","root","digital_hunter")

