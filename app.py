from flask import Flask
from modules.home import _home
from modules.register import _register
from modules.login import _login
from modules.surveillance import _surveillance

app = Flask(__name__)


app.register_blueprint(_home)
app.register_blueprint(_register, url_prefix="/register")
app.register_blueprint(_login, url_prefix="/login")
app.register_blueprint(_surveillance, url_prefix="/surveillance")

if __name__ == "__main__":
    app.run(debug=True)

