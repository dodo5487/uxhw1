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
    
    name = request.form["usr"]
    password = request.form["pwd"]
    position = db.login(name,password)
    if position != "": 
        if position == "user":
            session[f"{name}"] = name
            return redirect(f"/user/{name}")
        if position == "admin":
            session[f"{name}"] = name
            return redirect(f"/admin/{name}")
    else:
        return redirect("/login")

@app.route("/user/<name>") # 搭配 session 來使用
def user(name):
    if name in session:
        return render_template("user.html", user = name)  
    else:
        return redirect("/")

@app.route("/admin/<name>")
def admin(name):
    if name in session:
        return render_template("admin.html", user = name)  
    else:
        return redirect("/")

@app.route("/signout")
def signout(name):
    # 移除 Session 中的會員資訊
    del session[f"{name}"]
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)