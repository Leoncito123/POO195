from flask import Flask

#instacia de la clase Flask
app = Flask(__name__)

#Definir la ruta de la pagina 
if __name__ == '__main__':
    app.run(port=3000, debug=True)