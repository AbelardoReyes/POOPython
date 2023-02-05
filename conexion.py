import pymongo
from os import remove
class Conexion:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
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
        except:
            input("Conexion fallida")
            return False
    
    def insertarUnoMongo(self,database_entry,client,DATABASE,destination):
        collection = client[DATABASE][destination]
        collection.insert_one(database_entry)
        enter = input("Presione una tecla para continuar...")
        print("Guardado exitoso")
    
    def insertarMuchosMongo(self,diccionario,client,DATABASE,destination):
        try:
            collection = client[DATABASE][destination]
            li = []
            count = 0
            for i in diccionario:
                li.append(i)
                count += 1
            collection.insert_many(li)
            remove("productos2.json")
            enter = input("Presiona una te tecla...")
        except:
            input("Error al guardar")
        
    def mostrarMongo(self,client,DATABASE,destination):
        collection = client[DATABASE][destination]
        for i in collection.find():
            print(i)
        enter = input("Presione una tecla para continuar...")
 
