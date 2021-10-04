# -*- coding: utf-8 -*-

from flask_classful import FlaskView,route
from flask import request,jsonify
from flask_cors import cross_origin
import json # pip install json
import pyodbc # pip install pyodbc
import sys

class cartRoutes(FlaskView):

    @route("/api/getCartData",methods=['POST'])
    def getProfileData(self):
        if request.method == 'POST':
            try:
                TableData = request.get_json(force=False,silent=True)  
                searchText = TableData['SearchText']
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("getCartMedecine '%"+ searchText + "%'")
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


    @route("/api/saveCartData", methods=['POST'])
    def updateProfile(self):
        if request.method == 'POST':
            try:
                TableData = request.get_json(force=False,silent=True)
                user = TableData['user']
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("SaveUserCartData '"+TableData['MedicineID'] 
                               +"','" +TableData['UserName']+"','"+TableData['Quantity']+"'")
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
                
                
    @route("/api/CartBilling", methods=['POST'])
    def updateProfile(self):
        if request.method == 'POST':
            try:
                TableData = request.get_json(force=False,silent=True)
                user = TableData['user']
                connection = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=demo;uid=admin;pwd=Intel@sa$123')# Creating Cursor  
                cursor = connection.cursor()
                cursor.execute("cartBilling '"+TableData['UserName'] +"'")
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
 
