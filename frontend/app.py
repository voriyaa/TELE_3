from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

base_url = "http://localhost:2000"

# Код доступа
ACCESS_CODE = "12345"

# Ваша база данных тарифов
tariffs = [
    {"name": "Тариф 1", "price": 100},
    {"name": "Тариф 2", "price": 200},
    {"name": "Тариф 3", "price": 300}
]


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/admin", methods=["GET", "POST"])
def admin_access():
    error = None
    if request.method == "POST":
        access_code = request.form.get("access_code")
        if access_code == ACCESS_CODE:
            return redirect(url_for('admin_login'))  # Перенаправляем на страницу входа администратора
        else:
            error = "Неверный код доступа"
    return render_template('admin_key.html', error=error)


@app.route("/user/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        # Обработка отправленной формы входа пользователя
        username = request.form.get("username")
        password = request.form.get("password")
        # Здесь может быть логика проверки учетных данных пользователя
        return redirect(url_for('user_dashboard', username=username))
    else:
        return render_template('user_login.html')


@app.route("/user/register", methods=["GET", "POST"])
def user_register():
    if request.method == "POST":
        # Обработка отправленной формы регистрации пользователя
        username = request.form.get("username")
        password = request.form.get("password")
        # Здесь может быть логика для регистрации пользователя
        return redirect(url_for('user_dashboard', username=username))
    else:
        return render_template('user_register.html', tariffs=tariffs)


@app.route("/user/<username>/dashboard")
def user_dashboard(username):
    return render_template('user_dashboard.html', username=username)


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        # Обработка отправленной формы входа администратора
        username = request.form.get("username")
        password = request.form.get("password")
        # Здесь может быть логика проверки учетных данных администратора
        return redirect(url_for('admin_dashboard', username=username))
    else:
        return render_template('admin_login.html')


@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    if request.method == "POST":
        # Обработка отправленной формы регистрации администратора
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        dob = request.form.get("dob")
        passport_number = request.form.get("passport_number")
        gender = request.form.get("gender")
        username = request.form.get("username")
        password = request.form.get("password")

        # Здесь может быть логика для регистрации администратора в базе данных

        return redirect(url_for('admin_dashboard', username=username))
    else:
        return render_template('admin_register.html')


@app.route("/admin/<username>/dashboard")
def admin_dashboard(username):
    return render_template('admin_dashboard.html', username=username, tariffs=tariffs)


if __name__ == "__main__":
    app.run(debug=True)
