from blueprints.admin_api import adm
from blueprints.user_api import user
from App import app, docs
from src.Tools.DocsRegister import docs_register
docs_register(app, docs, adm)
docs_register(app, docs, user)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
