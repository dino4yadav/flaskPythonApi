from flask_classful import FlaskView,route
from flask import request,jsonify
from flask_cors import cross_origin
import json # pip install json
import pyodbc # pip install pyodbc
import sys

class profileRoutes(FlaskView):

    @route("/api/getProfileData",methods=['POST'])
    def getProfileData(self):
        if request.method == 'POST':
            try:
                TableData = request.get_json(force=False,silent=True)  
                user = TableData['user']
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM registration where UserName = '" + user +"'")
                rows = cursor.fetchall()
                GetTableData = []
                for row in rows:
                  GetTableData.append([x for x in row])
                cursor.close()
                connection.close()
                response = jsonify(GetTableData)
                response.headers.add("Access-Control-Allow-Origin", "*")
                response.headers.add('Access-Control-Allow-Headers', "*")
                response.headers.add('Access-Control-Allow-Methods', "*")
                return response
            except pyodbc.Error as ex:
                response = jsonify('there is some error' + ex)


    @route("/api/updateProfile", methods=['POST'])
    def updateProfile(self):
        if request.method == 'POST':
            try:
                TableData = request.get_json(force=False,silent=True)
                user = TableData['user']
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("UpdateProfileData '"+TableData['userID'] 
                               +"','" +TableData['user']+"','"+TableData['pass']
                               +"','"+TableData['email']+"','"+TableData['phone']+"'")
                rows = cursor.fetchall()
                GetTableData = []
                for row in rows:
                  GetTableData.append([x for x in row])
                cursor.close()
                connection.close()
                response = jsonify(GetTableData)
                response.headers.add("Access-Control-Allow-Origin", "*")
                response.headers.add('Access-Control-Allow-Headers', "*")
                response.headers.add('Access-Control-Allow-Methods', "*")
                return response
            except Exception as ex:
                response = jsonify(ex)
 
