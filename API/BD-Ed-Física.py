import sqlite3

conexion = sqlite3.connect('usrs_y_ejercicios.db')

#Creacián de las Tablas para ejercicios y usuarios
conexion.execute('CREATE TABLE ejercicios(nombre STRING PRIMARY KEY, intensidad STRING, duración INTEGER, edad_objetivo INTEGER, músculos_trabajados STRING)')
conexion.execute('CREATE TABLE usuarios(id INTEGER PRIMARY_KEY, usuario STRING, E_MAIL STRING, rol TEXT NOT NULL)')

#Creación de tabla datos de los usuarios
conexion.execute('CREATE TABLE info_usr(id_usr INTEGER PRIMARY KEY, nombre TEXT NOT NULL, fecha_nacimiento TEXT NOT NULL, FOREIGN KEY(id_usr) REFERENCES id(usuarios))')

conexion.close()