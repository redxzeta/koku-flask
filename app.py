from flask import *
from flask_cors import *

from api.koku import koku
from util.error_advice import advice

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# routes and error handle routes

app.register_blueprint(koku)
app.register_blueprint(advice)

if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()
