import pymongo

def login(student_id:str,password:str):
    client = pymongo.MongoClient("mongodb+srv://root:vM6V8rHqAy1bNjGp@uxhw1cluster.85qhe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # 選擇要操作的資料庫
    db = client.uxhw1
    # 選擇要存取的 table
    collection = db.accounts
    cursor = collection.find()
    for data in cursor:
        if data["student_id"] == student_id and data["password"] == password:
            return data
    return ""

def insert_many():
    client = pymongo.MongoClient("mongodb+srv://root:vM6V8rHqAy1bNjGp@uxhw1cluster.85qhe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # 選擇要操作的資料庫
    db = client.uxhw1
    # 選擇要存取的 table
    collection = db.accounts
    collection.insert_many([
        {"student_id":"P12121212","name":"陳小明","password":"1234","position":"user","car":"ABC-1989","until":"2022/9/30","violation":0,"picture":"/static/img/student.jpg"},
        {"student_id":"P24242424","name":"王怡君","password":"1234","position":"student_admin","car":"DEF-1234","until":"2022/9/30","violation":0,"picture":"/static/img/student_admin.jpg"},
        {"student_id":"P36363636","name":"田約翰","password":"1234","position":"admin","car":None,"until":None,"violation":None,"picture":"/static/img/admin.jpg"},
    ])

def delete():
    client = pymongo.MongoClient("mongodb+srv://root:vM6V8rHqAy1bNjGp@uxhw1cluster.85qhe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # 選擇要操作的資料庫
    db = client.uxhw1
    # 選擇要存取的 table
    collection = db.accounts
    collection.drop()

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

# insert_many()
# delete()