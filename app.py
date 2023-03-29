from flask import Flask
from modules.register import _register
from modules.user_list import _user_list

app = Flask(__name__)


app.register_blueprint(_register, url_prefix="/register")
app.register_blueprint(_user_list, url_prefix="/user_list")

if __name__ == "__main__":
    app.run(debug=True)

