from flask import Flask
from flask_cors import CORS
from src.common.database import Database

from src.Item.item_views import item_bp

app = Flask(__name__)
CORS(app)
app.secret_key = "Jimmy"

@app.before_first_request
def init():
    Database.go()

app.register_blueprint(item_bp)


if __name__ == '__main__':
    app.run()
