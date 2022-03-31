import pymongo

def login(name:str,password:str):
    client = pymongo.MongoClient("mongodb+srv://root:vM6V8rHqAy1bNjGp@uxhw1cluster.85qhe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # 選擇要操作的資料庫
    db = client.uxhw1
    # 選擇要存取的 table
    collection = db.accounts
    cursor = collection.find()
    for data in cursor:
        if data["name"] == name and data["password"] == password:
            return data["position"]
    return ""

def insert():
    client = pymongo.MongoClient("mongodb+srv://root:vM6V8rHqAy1bNjGp@uxhw1cluster.85qhe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # 選擇要操作的資料庫
    db = client.uxhw1
    # 選擇要存取的 table
    collection = db.accounts
    collection.insert_many([
        {"name":"godpoor","password":"1234","position":"user"},
        {"name":"dog","password":"1234","position":"admin"},
        {"name":"jee8","password":"1234","position":"user"}
    ])

def signup(name:str,password:str): # NOT finish
    client = pymongo.MongoClient("mongodb+srv://root:vM6V8rHqAy1bNjGp@uxhw1cluster.85qhe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # 選擇要操作的資料庫
    db = client.uxhw1
    # 選擇要存取的 table
    collection = db.accounts
    cursor = collection.find()
    for data in cursor:
        if data["name"] == name and data["password"] == password:
            return data["position"]
    return ""
# login()