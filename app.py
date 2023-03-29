from flask import Flask
from modules.register import _register

app = Flask(__name__)


app.register_blueprint(_register, url_prefix="/register")

if __name__ == "__main__":
    app.run(debug=True)

