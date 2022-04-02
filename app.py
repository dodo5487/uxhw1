import re
from flask import Flask , request ,session
from flask import render_template , redirect , url_for
import json , ast , time , db

app = Flask(
    __name__,
    static_folder="static", # 放置靜態物件的名稱
    static_url_path="/static",
)

app.secret_key = "nckuuxhw"  # 設定 Session 的密鑰

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup_handle")
def signup_handle():
    return ""

@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/handle",methods=["POST"])
def handle():
    
    student_id = request.form["usr"]
    password = request.form["pwd"]
    dict = db.login(student_id,password) # 從資料庫回傳使用者資料 dict
    position = dict["position"]
    if position != "": 
        if position == "user":
            session["id"] = student_id
            session["name"] = dict["name"]
            session["car"] = dict["car"]
            session["until"] = dict["until"]
            session["picture"] = dict["picture"]
            return redirect(f"/user/{student_id}")
        if position == "admin":
            session["id"] = student_id
            session["name"] = dict["name"]
            return redirect(f"/admin/{student_id}")
    else:
        return redirect("/login")

@app.route("/user/<student_id>") # 搭配 session 來使用
def user(student_id):
    try:
        if session["id"] == student_id:
            return render_template("user_page.html", student_id = student_id , name = session["name"] , picture = session["picture"])  
    except:
        return redirect("/")

@app.route("/admin/<student_id>")
def admin(student_id):
    try:
        if session["id"] == student_id:
            return render_template("admin.html", student_id = student_id)  
    except:
        return redirect("/")

@app.route("/signout")
def signout(name):
    # 移除 Session 中的會員資訊 
    del session[f"{name}"]
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)