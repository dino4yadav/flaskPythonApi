#!/usr/bin/env python

from flask import Flask
from src.flask_api import flask_api
from src.registration_api import registration_api
from src.profile_api import profile_api
from src.cart_api import cart_api
from flask_cors import CORS

app = Flask(__name__)
flask_api.flaskRoutes.register(app,route_base = '/')
registration_api.registrationRoutes.register(app,route_base = '/')
#profile_api.profileRoutes.register(app,route_base = '/')
#cart_api.cartRoutes.register(app, route_base = '/')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True, threaded=True)
