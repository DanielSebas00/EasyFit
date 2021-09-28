from flask import Flask, request, jsonify
from flask_restful import Resource, Api,reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
trainings = {}

class Training(Resource):
    def get(self, training_id):

        return jsonify(
            
        )

    def put(selft, training_id):

        return jsonify(
            
        )

    def delete(self, training_id):
        
        return jsonify(
            
        )

class TrainingList(Training):
    def get(self):
        conexion = sqlite3.connect('usrs_y_ejercicios.db')
        sql = '''select * from ejercicios limit 1000'''
        cur = conexion.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conexion.close()

        parseArray = []
        for row in rows:
            nombre = row[0]
            intensidad = row[1]
            duración = row[2]
            edad_objetivo = row[3]
            músculos_trabajados = row[4]
            dict = {
                "nombre": nombre,
                "intensidad": intensidad,
                "duración" : duración,
                "edad_objetivo": edad_objetivo,
                "músculos_trabajados": músculos_trabajados
            }
            parseArray.append(dict)

        return jsonify(
           *parseArray
        )
    def post(self):
        json_data = request.get_json(force=True)
       
        nombre = json_data['nombre']
        intensidad = json_data['intensidad']
        duración = json_data['duración']
        edad_objetivo = json_data['edad_objetivo']
        músculos_trabajados = json_data['músculos_trabajados']

        conexion = sqlite3.connect('usrs_y_ejercicios.db')

        sql = ''' INSERT INTO ejercicios(nombre,intensidad,duración, edad_objetivo,músculos_trabajados)
              VALUES(?,?,?,?,?) '''
        cur = conexion.cursor()
        cur.execute(sql, (
            nombre,
            intensidad,
            duración,
            edad_objetivo,
            músculos_trabajados
        ))
        conexion.commit()
        conexion.close()
        return jsonify(
            {
                "nombre": nombre,
                "intensidad": intensidad,
                "duración" : duración,
                "edad_objetivo": edad_objetivo,
                "músculos_trabajados": músculos_trabajados
            }
        )

api.add_resource(Training, '/trainings/<string:training_id>')
api.add_resource(TrainingList, '/trainings/')

if __name__ == '__main__':
    app.run(debug=True)