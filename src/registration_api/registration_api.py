from flask_classful import FlaskView,route
from flask import request,jsonify
from flask_cors import cross_origin
import json # pip install json
import pyodbc # pip install pyodbc

class registrationRoutes(FlaskView):

    @route("/api/getUser",methods=['POST'])
    def getDataFromDB(self):
        if request.method == 'POST':
            try:
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM registration")
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
                response = jsonify(ex)


    @route("/api/register", methods=['POST'])
    def registration(self):
        if request.method == 'POST':
            try:
                TableData = request.get_json(force=False,silent=True)  
                user = TableData['user']
                passw = TableData['pass']
                phone = TableData['phone']
                email = TableData['pass']
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("insert into registration select '" + user +"','" + passw +"'," + phone +",'" + email + "'" )
                connection.commit()
                cursor.close()
                connection.close()
                response = jsonify('TableData')
                response.headers.add("Access-Control-Allow-Origin", "*")
                response.headers.add('Access-Control-Allow-Headers', "*")
                response.headers.add('Access-Control-Allow-Methods', "*")
                return response
            except pyodbc.Error as ex:
                return jsonify('Error')
 
