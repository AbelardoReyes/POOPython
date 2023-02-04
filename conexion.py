import pymongo


class Conexion:
    def __init__(self) -> None:
        pass

    def iniciarConexion(self):
        MONGODB_TIMEOUT = 1000
        MONGO_DATABASE = "tienda"
        URI_CONNECTION = "mongodb+srv://admin:administrador@cluster0.fzaqu9v.mongodb.net/?retryWrites=true&w=majority"
        try:
            client = pymongo.MongoClient(
                URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT)
            client.server_info()
            return client
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)
            enter = input("Presione una tecla para continuar...")
        except pymongo.errors.ConnectionFailure as err:
            print(err)
            enter = input("Presione una tecla para continuar...")
    
    def insertarUnoMongo(self,database_entry,client,DATABASE,destination):
        collection = client[DATABASE][destination]
        collection.insert_one(database_entry)
        enter = input("Presione una tecla para continuar...")
        print("Guardado exitoso")
        
    def mostrarMongo(self,client,DATABASE,destination):
        collection = client[DATABASE][destination]
        for i in collection.find():
            print(i)
        enter = input("Presione una tecla para continuar...")
 
