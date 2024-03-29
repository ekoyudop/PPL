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
    
# @app.route('/register')
# def register():
#     token_receive = request.cookies.get("mytoken")
#     try:
#         payload = jwt.decode(
#             token_receive, 
#             SECRET_KEY, 
#             algorithms=["HS256"])
        
#         return redirect(url_for("dashboard"))
    
#     except jwt.ExpiredSignatureError:
#         return render_template("register.html")
#     except jwt.exceptions.DecodeError:
#         return render_template("register.html")
    
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

        all_weapons1 = db.weapon.find()
        all_weapons2 = db.weapon.find()
        all_weapons3 = db.weapon.find()
        total_tersedia = sum(weapon.get("tersedia", 0) for weapon in all_weapons1)
        total_dipakai = sum(weapon.get("dipakai", 0) for weapon in all_weapons2)
        total_rusak = sum(weapon.get("rusak", 0) for weapon in all_weapons3)

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
                               weapon_list4 = weapon_list4,
                               total_tersedia = total_tersedia,
                               total_dipakai = total_dipakai,
                               total_rusak = total_rusak)
    
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

        history = db.history.find()
        
        return render_template("history.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               history = history)
    
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
    
@app.route('/detail/<string:weapon_id>', methods = ['GET'])
def detail(weapon_id):
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

        weapon_detail = db.weapon.find_one({'_id': ObjectId(weapon_id)})
        history = db.history.find({'weapon': weapon_detail['name']})
        
        return render_template("detail.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_detail = weapon_detail,
                               history = history)
    
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
                role = user_info.get("role")
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        if role not in ["admin"]:
            return redirect(url_for("dashboard"))

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
    
@app.route('/edit/<string:weapon_id>', methods = ['GET'])
def edit(weapon_id):
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
                role = user_info.get("role")
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        if role not in ["admin"]:
            return redirect(url_for("dashboard"))

        weapon_detail = db.weapon.find_one({'_id': ObjectId(weapon_id)})
        
        return render_template("edit_item.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               weapon_detail = weapon_detail)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/manage_user', methods = ['GET'])
def manage_user():
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
                role = user_info.get("role")
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        if role not in ["admin"]:
            return redirect(url_for("dashboard"))

        user_list = db.user.find()
        
        return render_template("manage_user.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               user_list = user_list)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/edit2/<string:user_id>', methods = ['GET'])
def edit2(user_id):
    token_receive = request.cookies.get("mytoken")
    try:
        if token_receive:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.user.find_one({"username": payload["id"]})
            if user_info:
                is_admin = user_info.get("role") == "admin"
                logged_in = True
                role = user_info.get("role")
            else:
                is_admin = False
                logged_in = False
        else:
            user_info = None
            is_admin = False
            logged_in = False

        if role not in ["admin"]:
            return redirect(url_for("dashboard"))

        user_detail = db.user.find_one({'_id': ObjectId(user_id)})
        
        return render_template("edit_user.html", 
                               user_info = user_info,
                               is_admin = is_admin,
                               logged_in = logged_in,
                               user_detail = user_detail)
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))

# @app.route("/api/register", methods=["POST"])
# def api_register():
#     username_receive = request.form["username_give"]

#     existing_user = db.user.find_one({"username": username_receive})
#     if existing_user:
#         msg = f"An account with id {username_receive} already exists!"
#         return jsonify({"result": "failure", "msg": msg})

#     password_receive = request.form["password_give"]
#     role_receive = request.form.get("role_give")

#     password_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()

#     db.user.insert_one({
#         "username": username_receive, 
#         "password": password_hash, 
#         "role": role_receive
#     })

#     return jsonify({"result": "success"})

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
    
@app.route('/detail_pakai/<string:weapon_id>', methods = ['PUT'])
def detail_pakai(weapon_id):
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        jumlah_receive = int(request.form["jumlah_give"]) 
        username_receive = request.form["username_give"]

        db.weapon.update_one(
            {'_id': ObjectId(weapon_id)},
            {
                '$set': {
                    "tersedia": db.weapon.find_one({'_id': ObjectId(weapon_id)})["tersedia"] - jumlah_receive,
                    "dipakai": db.weapon.find_one({'_id': ObjectId(weapon_id)})["dipakai"] + jumlah_receive
                }
            }
        )

        weapon_data = db.weapon.find_one({'_id': ObjectId(weapon_id)})
        weapon_name = weapon_data.get("name")

        mytime = datetime.now().strftime("%H:%M:%S - %d %B %Y")

        history_message = f"{jumlah_receive} unit {weapon_name} diambil untuk dipakai"
        history_message2 = f"{username_receive} | {mytime}"
        today = datetime.now()

        db.history.insert_one({
            "weapon": weapon_name,
            "message": history_message,
            "by" : history_message2,
            "timestamp": today
        })

        return jsonify({"result": "success"})
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/detail_kembalikan/<string:weapon_id>', methods = ['PUT'])
def detail_kembalikan(weapon_id):
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        jumlah_receive = int(request.form["jumlah_give"]) 
        username_receive = request.form["username_give"]

        db.weapon.update_one(
            {'_id': ObjectId(weapon_id)},
            {
                '$set': {
                    "tersedia": db.weapon.find_one({'_id': ObjectId(weapon_id)})["tersedia"] + jumlah_receive,
                    "dipakai": db.weapon.find_one({'_id': ObjectId(weapon_id)})["dipakai"] - jumlah_receive
                }
            }
        )

        weapon_data = db.weapon.find_one({'_id': ObjectId(weapon_id)})
        weapon_name = weapon_data.get("name")

        mytime = datetime.now().strftime("%H:%M:%S - %d %B %Y")

        history_message = f"{jumlah_receive} unit {weapon_name} dikembalikan dengan kondisi normal"
        history_message2 = f"{username_receive} | {mytime}"
        today = datetime.now()

        db.history.insert_one({
            "weapon": weapon_name,
            "message": history_message,
            "by" : history_message2,
            "timestamp": today
        })

        return jsonify({"result": "success"})
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route('/detail_kembalikan_rusak/<string:weapon_id>', methods = ['PUT'])
def detail_kembalikan_rusak(weapon_id):
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        jumlah_receive = int(request.form["jumlah_give"])
        username_receive = request.form["username_give"]

        db.weapon.update_one(
            {'_id': ObjectId(weapon_id)},
            {
                '$set': {
                    "rusak": db.weapon.find_one({'_id': ObjectId(weapon_id)})["rusak"] + jumlah_receive,
                    "dipakai": db.weapon.find_one({'_id': ObjectId(weapon_id)})["dipakai"] - jumlah_receive
                }
            }
        )
        
        weapon_data = db.weapon.find_one({'_id': ObjectId(weapon_id)})
        weapon_name = weapon_data.get("name")

        mytime = datetime.now().strftime("%H:%M:%S - %d %B %Y")

        history_message = f"{jumlah_receive} unit {weapon_name} dikembalikan dengan kondisi rusak"
        history_message2 = f"{username_receive} | {mytime}"
        today = datetime.now()

        db.history.insert_one({
            "weapon": weapon_name,
            "message": history_message,
            "by" : history_message2,
            "timestamp": today
        })

        return jsonify({"result": "success"})
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))

@app.route("/add_item", methods=["POST"])
def add_item():
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])

        itemname_receive = request.form["itemname_give"]
        kategori_receive = request.form["kategori_give"]
        tersedia_receive = int(request.form["tersedia_give"])
        dipakai_receive = int(request.form["dipakai_give"])
        rusak_receive = int(request.form["rusak_give"])
        image_receive = request.files["image_give"]

        today = datetime.now()
        mytime = today.strftime("%Y-%m-%d-%H-%M-%S")

        if image_receive:
            extension = image_receive.filename.split('.')[-1]
            filename = f'static/post-{mytime}.{extension}'
            image_receive.save(filename)


        existing_course = db.weapon.find_one({"name": itemname_receive})
        if existing_course:
            return jsonify({"result": "error", "message": "Item sudah ada."})

        db.weapon.insert_one({
            "name": itemname_receive,
            "type": kategori_receive,
            "tersedia": tersedia_receive,
            "dipakai": dipakai_receive,
            "rusak": rusak_receive,
            "image": filename if image_receive else None
        })

        mytime = datetime.now().strftime("%H:%M:%S - %d %B %Y")

        history_message = f"{itemname_receive} telah berhasil ditambahkan (Tersedia: {tersedia_receive} | Dipakai: {dipakai_receive} | Rusak: {rusak_receive})"
        history_message2 = f"Admin | {mytime}"

        db.history.insert_one({
            "weapon": itemname_receive,
            "message": history_message,
            "by" : history_message2,
            "timestamp": today
        })

        return jsonify({"result": "success"})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("discover"))
    
@app.route('/delete_item/<string:item_id>', methods=['DELETE'])
def delete_item(item_id):
    from datetime import datetime
    try:
        weapon_data = db.weapon.find_one({'_id': ObjectId(item_id)})
        weapon_name = weapon_data.get("name")

        mytime = datetime.now().strftime("%H:%M:%S - %d %B %Y")

        history_message = f"{weapon_name} telah berhasil dihapus"
        history_message2 = f"Admin | {mytime}"
        today = datetime.now()

        db.history.insert_one({
            "weapon": weapon_name,
            "message": history_message,
            "by" : history_message2,
            "timestamp": today
        })

        result = db.weapon.delete_one({'_id': ObjectId(item_id)})

        if result.deleted_count > 0:
            response = {'result': 'success', 'message': 'Item deleted successfully.'}
        else:
            response = {'result': 'error', 'message': 'Course not found.'}
    except Exception as e:
        response = {'result': 'error', 'message': str(e)}

    return jsonify(response)

@app.route('/edit_item/<string:weapon_id>', methods = ['PUT'])
def edit_item(weapon_id):
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        tersedia_receive = int(request.form["tersedia_give"]) 
        dipakai_receive = int(request.form["dipakai_give"]) 
        rusak_receive = int(request.form["rusak_give"]) 

        db.weapon.update_one(
            {'_id': ObjectId(weapon_id)},
            {
                '$set': {
                    "tersedia": tersedia_receive,
                    "dipakai": dipakai_receive,
                    "rusak": rusak_receive
                }
            }
        )

        weapon_data = db.weapon.find_one({'_id': ObjectId(weapon_id)})
        weapon_name = weapon_data.get("name")

        mytime = datetime.now().strftime("%H:%M:%S - %d %B %Y")

        history_message = f"Stock {weapon_name} telah berhasil diubah (Tersedia: {tersedia_receive} | Dipakai: {dipakai_receive} | Rusak: {rusak_receive})"
        history_message2 = f"Admin | {mytime}"
        today = datetime.now()

        db.history.insert_one({
            "weapon": weapon_name,
            "message": history_message,
            "by" : history_message2,
            "timestamp": today
        })

        return jsonify({"result": "success"})
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))
    
@app.route("/add_user", methods=["POST"])
def add_user():
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])

        username_receive = request.form["username_give"]
        password_receive = request.form["password_give"]
        nama_receive = request.form["nama_give"]
        email_receive = request.form["email_give"]
        nrp_receive = request.form["nrp_give"]
        kesatuan_receive = request.form["kesatuan_give"]
        notelepon_receive = request.form["notelepon_give"]

        password_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()

        existing_user = db.user.find_one({"username": username_receive})
        if existing_user:
            return jsonify({"result": "error", "message": "User sudah ada."})

        db.user.insert_one({
            "username": username_receive,
            "password": password_hash,
            "password2": password_receive,
            "nama": nama_receive,
            "email": email_receive,
            "nrp": nrp_receive,
            "kesatuan": kesatuan_receive,
            "notelepon": notelepon_receive
        })

        return jsonify({"result": "success"})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("discover"))
    
@app.route('/delete_user/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    from datetime import datetime
    try:
        result = db.user.delete_one({'_id': ObjectId(user_id)})

        if result.deleted_count > 0:
            response = {'result': 'success', 'message': 'Item deleted successfully.'}
        else:
            response = {'result': 'error', 'message': 'Course not found.'}
    except Exception as e:
        response = {'result': 'error', 'message': str(e)}

    return jsonify(response)

@app.route('/edit_user/<string:user_id>', methods = ['PUT'])
def edit_user(user_id):
    from datetime import datetime
    token_receive = request.cookies.get("mytoken")
    try:
        username_receive = request.form["username_give"]
        password_receive = request.form["password_give"]
        nama_receive = request.form["nama_give"]
        email_receive = request.form["email_give"]
        nrp_receive = request.form["nrp_give"]
        kesatuan_receive = request.form["kesatuan_give"]
        notelepon_receive = request.form["notelepon_give"]

        password_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()

        db.user.update_one(
            {'_id': ObjectId(user_id)},
            {
                '$set': {
                    "username": username_receive,
                    "password": password_hash,
                    "password2": password_receive,
                    "nama": nama_receive,
                    "email": email_receive,
                    "nrp": nrp_receive,
                    "kesatuan": kesatuan_receive,
                    "notelepon": notelepon_receive
                }
            }
        )
        return jsonify({"result": "success"})
    
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)