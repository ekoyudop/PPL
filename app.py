import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from bson import ObjectId

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

SECRET_KEY = "ALUTSISTA"

@app.route('/')
def index():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(
            token_receive, 
            SECRET_KEY, 
            algorithms=["HS256"])
        
        return redirect(url_for("dashboard"))
    
    except jwt.ExpiredSignatureError:
        return render_template("welcome.html", msg="Your token has expired")
    except jwt.exceptions.DecodeError:
        return render_template("welcome.html", msg="There was problem logging you in")
    
@app.route('/register')
def register():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(
            token_receive, 
            SECRET_KEY, 
            algorithms=["HS256"])
        
        return redirect(url_for("dashboard"))
    
    except jwt.ExpiredSignatureError:
        return render_template("register.html")
    except jwt.exceptions.DecodeError:
        return render_template("register.html")
    
@app.route('/login')
def login():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(
            token_receive, 
            SECRET_KEY, 
            algorithms=["HS256"])
        
        return redirect(url_for("dashboard"))
    
    except jwt.ExpiredSignatureError:
        return render_template("login.html")
    except jwt.exceptions.DecodeError:
        return render_template("login.html")
    
@app.route('/dashboard', methods = ['GET'])
def dashboard():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        weapon_list1 = db.weapon.find({"type": "Senjata Ringan"})
        weapon_list2 = db.weapon.find({"type": "Meriam/Roket/Rudal"})
        weapon_list3 = db.weapon.find({"type": "Kendaraan Tempur"})
        weapon_list4 = db.weapon.find({"type": "Pesawat Terbang"})
        
        return render_template("dashboard.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_list1 = weapon_list1,
                               weapon_list2 = weapon_list2,
                               weapon_list3 = weapon_list3,
                               weapon_list4 = weapon_list4)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/history', methods = ['GET'])
def history():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False
        
        return render_template("history.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/armory/1', methods = ['GET'])
def armory1():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        weapon_list1 = db.weapon.find({"type": "Senjata Ringan"})
        
        return render_template("armory1.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_list1 = weapon_list1)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/armory/2', methods = ['GET'])
def armory2():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        weapon_list2 = db.weapon.find({"type": "Meriam/Roket/Rudal"})
        
        return render_template("armory2.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_list2 = weapon_list2)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/armory/3', methods = ['GET'])
def armory3():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        weapon_list3 = db.weapon.find({"type": "Kendaraan Tempur"})
        
        return render_template("armory3.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_list3 = weapon_list3)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))

@app.route('/armory/4', methods = ['GET'])
def armory4():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        weapon_list4 = db.weapon.find({"type": "Pesawat Terbang"})
        
        return render_template("armory4.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_list4 = weapon_list4)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))

@app.route('/manage_armory', methods = ['GET'])
def manage_armory():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        weapon_list = db.weapon.find()
        
        return render_template("manage_armory.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_list = weapon_list)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))

@app.route("/api/register", methods=["POST"])
def api_register():
    username_receive = request.form["username_give"]

    existing_user = db.user.find_one({"id": username_receive})
    if existing_user:
        msg = f"An account with id {username_receive} already exists!"
        return jsonify({"result": "failure", "msg": msg})

    password_receive = request.form["password_give"]
    role_receive = request.form.get("role_give")

    password_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()

    db.user.insert_one({
        "username": username_receive, 
        "password": password_hash, 
        "role": role_receive
    })

    return jsonify({"result": "success"})

@app.route("/api/login", methods=["POST"])
def api_login():
    username_receive = request.form["username_give"]
    password_receive = request.form["password_give"]

    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()

    result = db.user.find_one({
        "username": username_receive, 
        "password": pw_hash
    }, {"role": 1})

    if result:
        role_user = result.get("role", None)

        payload = {
            "id": username_receive,
            "role": role_user,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60),
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return jsonify({
            "result": "success",
            "token": token
        })
    else:
        return jsonify({
            "result": "fail", 
            "msg": "your username or password is incorrect"
        })

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)