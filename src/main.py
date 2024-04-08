# main.py
from flask import Flask
from blueprints.user_api import user as page_primer
from blueprints.admin_api import admin as primery_api


app = Flask(__name__)
app.register_blueprint(page_primer)
app.register_blueprint(primery_api)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run(debug=True)