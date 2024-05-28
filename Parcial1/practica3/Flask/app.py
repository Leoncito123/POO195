from flask import Flask, request

#instacia de la clase Flask
app = Flask(__name__)

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