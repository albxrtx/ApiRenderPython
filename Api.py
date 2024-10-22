# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:11:55 2024

@author: DAM
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/lista1",methods = ["GET"])
def obtener_lista1():
    datos = {
        "nombre" : "Sebas",
        "edad": 19,
        "Residencia": "Seseña"}
    return jsonify(datos)

@app.route("/api/lista2", methods = ["GET"])
def obtener_lista2():
    lista_datos = [
        {"nombre" : "Sebas","edad": 19,"Residencia": "Seseña"},
        {"nombre" : "Javi","edad": 19,"Residencia": "Seseña"},
        {"nombre" : "Manu","edad": 19,"Residencia": "Cuidad Real"},
        {"nombre" : "Tymur","edad": 20,"Residencia": "Seseña"}]            
    return jsonify(lista_datos)
