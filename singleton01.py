# https://github.com/lazybird/django-solo you can compare it
import psycopg2

    
class DatabaseConnection:
    db_connection_pool = None

    # !TODO Энийг private буюу гаднаас хандах боломжгүй болгох. Зөвхөн энэ классын method-ууд дуудах л боломжтой байх. 
    def __init__(self, name:str, user:str, host:str, port: str, password: str = None):
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        try:
            with psycopg2.connect(database=name, user=user, password=password, port=port) as conn:
                self.db_connection_pool = conn
                print("New connection created")
                return conn
            
        except (psycopg2.DatabaseError, Exception) as error:
            raise error

    def __new__(cls):
        pass
    
    @classmethod
    def connect(self, name:str, user:str, host:str, port: str, password: str = None):
        port = int(port)

        if self.db_connection_pool == None:
            return self.__init__(self, name, user, password=password, host=host, port=port)
        
        print("--- Returing already connected connection")
        return self.db_connection_pool
    

for i in range(10):
    try:
        db = DatabaseConnection.connect(name="main-pro", host="localhost", user="postgres", port="5432")
        break  
    except Exception as err:
        print(f"Баазтай холбогдоход алдаа гарлаа: {err}")
        break  
