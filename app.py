from flask import Flask
from modules.home import _home
from modules.register import _register
from modules.login import _login
from modules.surveillance import _surveillance
from modules.user_list import _user_list

app = Flask(__name__)


app.register_blueprint(_home)
app.register_blueprint(_register, url_prefix="/register")
app.register_blueprint(_login, url_prefix="/login")
app.register_blueprint(_surveillance, url_prefix="/surveillance")
app.register_blueprint(_user_list, url_prefix="/user_list")

if __name__ == "__main__":
    app.run(debug=True)

