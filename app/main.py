from flask import Flask
from flask_cors import CORS

from app.route.map_route import app_blueprint

app = Flask(__name__, template_folder='templates', static_folder="static")
CORS(app)
app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5001)