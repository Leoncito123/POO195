from flask import Flask, request,render_template,jsonify, url_for,redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Variable del host de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bd_flask'
app.config['MYSQL_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'  
app.secret_key = 'mysecretkey'

#Variable de la conexion a la base de datos
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/albums', methods= ['POST'])
def guardaralbum():
    if request.method== 'POST':
        vtitulo = request.form['txtTitulo']
        vartista = request.form['artist']
        vano = request.form['ano']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO albums (titulo,artista,ano) VALUES (%s,%s,%s)',(vtitulo, vartista, vano))
        mysql.connection.commit()

        flash('Album guardado exitosamente')
        
        return redirect(url_for('index'))
    
    

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return 'Revisa tu sintaxis:No encontre nada'

if __name__ == '__main__':
    app.run(port=3000, debug=True)