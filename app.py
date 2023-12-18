import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient
import requests
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

@app.route('/', methods = ['GET'])
def login():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"id": payload["id"]})
            is_user = user_info.get("role") == "user"
            is_admin = user_info.get("role") == "admin"
            logged_in = True
        else:
            user_info = None
            is_admin = False
            logged_in = False
            is_member = False
        
        return render_template("login.html", 
                               user_info=user_info, 
                               is_user = is_user, 
                               is_admin = is_admin, 
                               logged_in = logged_in)
    
    except jwt.ExpiredSignatureError:
        return render_template("index.html", msg="Your token has expired")
    except jwt.exceptions.DecodeError:
        return render_template("index.html", msg="There was problem logging you in")
    
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)