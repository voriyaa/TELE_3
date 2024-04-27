from blueprints.admin_api import adm

from blueprints.user_api import user
from App import app, docs
from src.Tools.DocsRegister import docs_register
from src.Constants import Config

docs_register(app, docs, adm, '/api')
docs_register(app, docs, user, '/user')

if __name__ == "__main__":
    app.run(debug=True, host=Config.KNOWN_HOST, port=Config.PORT)
