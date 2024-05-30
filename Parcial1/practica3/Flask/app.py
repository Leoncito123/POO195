from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

#instacia de la clase Flask
app = Flask(__name__)

#Variable del host de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
#Variable de usuario de la base de datos
app.config['MYSQL_USER'] = 'root'
#Variable de la contraseña de la base de datos
app.config['MYSQL_PASSWORD'] = ''
#Variable de la base de datos
app.config['MYSQL_DB'] = 'bd_flask'

#Variable de la conexion a la base de datos
mysql = MySQL(app)


#Ruta basica
@app.route('/')
def principal ():
    return "Hola mundo"
#Ruta doble
@app.route('/usuario')
@app.route('/saludar')
def saludar():
    return "Hola usuario"

#Rutas con parametros
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola'+ ' '+ nombre + '!!!'

#Ruta para comprobar la conexion a la base de datos
@app.route('pruebaConexion')
def preubaConexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        data = cursor.fetchone()
        return jsonify({'satatus': 'Conexion exitosa', 'data':data})
    except Exception as ex:
        return jsonify({'status':'Error en la conexion', 'data': str(ex)})

#Definicon de metodos de trabajo 
@app.route('/formulario/', methods=['GET','POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar password por GET'
    elif request.metod == 'POST':
        return 'POST si es seguro para password'
#Manejo de excepciones en las rutas
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return 'Revisa tu sintaxis:No encontre nada'

#Definir la ruta de la pagina 
if __name__ == '__main__':
    app.run(port=3000, debug=True)