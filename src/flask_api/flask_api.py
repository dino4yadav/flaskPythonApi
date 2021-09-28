from flask_classful import FlaskView,route
from flask import request,Flask, redirect, url_for
from flask import jsonify

class flaskRoutes(FlaskView):

    def index(self):
    # http://localhost:5000/
        return "<h1>This is my indexpage</h1>"

    def secondpage(self):
    # http://localhost:5000/secondpage
        return "<h1>This is my second page</h1>" 
    
    def thirdpage(self,name):
    # dynamic route
    # http://localhost:5000/thirdpage/sometext
        return "<h1>This is my third page <br> welcome"+name+"</h1>"