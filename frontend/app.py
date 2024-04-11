import os
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request, \
    decode_token
from functools import wraps
import requests

from flask_cors import CORS

app = Flask(__name__)

app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['JWT_BLACKLIST_ENABLED'] = True
jwt = JWTManager(app)

base_url = "http://localhost:2000"

# Код доступа
ACCESS_CODE = "12345"

# Ваша база данных тарифов
tariffs = [
    {},
    {"tariff_id": "1", "name": "Тариф 1", "price": 100},
    {"tariff_id": "2", "name": "Тариф 2", "price": 200},
    {"tariff_id": "3", "name": "Тариф 3", "price": 300}
]


def extract_jwt_from_query_param():
    jwt_token = request.args.get('jwt')
    if jwt_token:
        return jwt_token
    return None


def jwt_required_from_query_param_admins(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        token = extract_jwt_from_query_param()
        if not token:
            return jsonify({"msg": "Missing JWT in query parameter"}), 401
        try:
            # Отправляем запрос к серверу API для проверки токена
            response = requests.post('http://93.175.7.10:5000/api/check_token', json={'token': token})
            if response.status_code != 200:
                return jsonify({"msg": "Invalid token"}), 401
            data = response.json()
            if data['username'] != kwargs['username']:
                return jsonify({"msg": "Invalid user for this token"}), 401
            if data['role'] != 'admin':
                return jsonify({"msg": "Insufficient role"}), 403
        except Exception as e:
            return jsonify({"msg": str(e)}), 401

        return fn(*args, **kwargs)

    return decorated


def jwt_required_from_query_param_users(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        token = extract_jwt_from_query_param()
        if not token:
            return jsonify({"msg": "Missing JWT in query parameter"}), 401

        try:
            decoded_token = decode_token(token)  # Декодируем токен
            jwt_identity = decoded_token.get('sub')  # Получаем идентификатор пользователя из токена
            jwt_role = decoded_token.get('role')  # Получаем роль пользователя из токена
            if jwt_identity != kwargs['username']:
                return jsonify({"msg": "Invalid user for this token"}), 401
            if jwt_role != 'user':  # Используем kwargs['role'] для проверки роли
                return jsonify({"msg": "Insufficient role"}), 403
        except Exception as e:
            return jsonify({"msg": str(e)}), 401

        return fn(*args, **kwargs)

    return decorated


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/admin", methods=["GET", "POST"])
def admin_access():
    error = None
    if request.method == "POST":
        access_code = request.form.get("access_code")
        if access_code == ACCESS_CODE:
            return redirect(url_for('admin_login'))
        else:
            error = "Неверный код доступа"
    return render_template('admin_key.html', error=error)


@app.route("/user/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

    else:
        return render_template('user_login.html')


@app.route("/user/register", methods=["GET", "POST"])
def user_register():
    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birth_date = request.form.get("birth_date")
        passport_id = request.form.get("passport_id")
        sex = request.form.get("sex")
        username = request.form.get("username")
        password = request.form.get("password")
    else:
        return render_template('user_register.html', tariffs=tariffs)


@app.route("/user/<username>/dashboard", methods=["POST", "GET"])
@jwt_required_from_query_param_users
def user_dashboard(username):
    if request.method == "GET":
        return render_template('user_dashboard.html', username=username)


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        #СЮДА
    else:
        return render_template('admin_login.html')


@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birth_date = request.form.get("birth_date")
        passport_id = request.form.get("passport_id")
        sex = request.form.get("sex")
        phone_number = request.form.get("phone_number")
        username = request.form.get("username")
        password = request.form.get("password")
    else:
        return render_template('admin_register.html')


@app.route("/admin/<username>/dashboard", methods=["POST", "GET"])
@jwt_required_from_query_param_admins
def admin_dashboard(username):
    if request.method == "GET":
        return render_template('admin_dashboard.html', username=username)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)